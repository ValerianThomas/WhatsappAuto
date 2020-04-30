import os
import time
from pymodm.connection import connect
from whatsapp.models.message import Message

connect(os.environ.get('MONGO_CLIENT',''), retryWrites=False)
list_of_messages = [('Test','test1'), ('Test','test2'), ('Test','test3')]

for message in list_of_messages:
    whatsapp_message = Message.objects.create(contact=message[0], message=message[1])
    whatsapp_message.save()
    time.sleep(2)