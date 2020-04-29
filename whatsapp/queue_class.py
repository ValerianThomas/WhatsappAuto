import os
import time
from threading import Thread
from multiprocessing import Queue
from pymodm.connection import connect

from whatsapp.models.message import Message
from whatsapp.driver_class import WhatsappMessaging

class MessageQueue:
    instance = None
    @classmethod
    def get_message_queue(cls):
        if cls.instance == None:
            cls.instance = MessageQueue()
        return cls.instance
    def __init__(self):
        '''
        Start queue instance 
        '''
        connect(os.environ.get('MONGO_CLIENT',''), retryWrites=False)
        self.thread = None
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
        if self.thread == None:
            self.thread = Thread(target=self.worker)
            self.thread.start()

