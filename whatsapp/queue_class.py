import os
from multiprocessing import Queue
from threading import Thread
from pymodm.connection import connect
from whatsapp.models.message import Message
from whatsapp.driver_class import WhatsappMessaging
import time
class MessageQueue:
    instanciated = False
    def __init__(self):
        '''
        Start queue instance 
        '''
        if not MessageQueue.instanciated:
            connect(os.environ.get('MONGO_CLIENT',''), retryWrites=False)
            MessageQueue.instanciated = True
            self.queue  = Queue()
            self.driver =  WhatsappMessaging()
    
    def get_message(self) -> None:
        '''
        Get message from DB and generates 
        '''
        return Message.objects.all().sort({ 'date' : 1 }).limit(1)
    
    def create_message(self, contact: str, message: str) -> None:
        '''
        Create a message in the DB and and add it to the worker queue.
        '''
        whatsapp_message = Message.objects.create(contact=contact, message=message)
        whatsapp_message.save()
        self.queue.put({'contact': whatsapp_message.contact, 'message': whatsapp_message.message, 'id': whatsapp_message._id})

    
    def delete_message(self, id: str) -> None:
        '''
        Delete a whatsapp message.
        '''
        whatsapp_message = Message.objects.get({'_id':id}) 
        whatsapp_message.delete()

    def worker(self) -> None:
        '''
        Worker queue running all messages requests.
        '''
        while  True:
            whatsapp_message = self.queue.get()
            if whatsapp_message:
                self.driver.send_message_to_contact(contact=whatsapp_message['contact'], message=whatsapp_message['message'])
                self.delete_message(whatsapp_message['id'])
                time.sleep(2)
            else:
                time.sleep(60)

    
    def start_worker(self) -> None:
        '''
        Start the worker whatsapp worker
        '''
        running_worker = Thread(target=self.worker)
        running_worker.start()

