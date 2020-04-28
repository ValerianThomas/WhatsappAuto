from whatsapp.driver_class import WhatsappMessaging
from whatsapp.queue_class import MessageQueue
import time

driver = WhatsappMessaging()
queue = MessageQueue()
qr = driver.get_login_qr_code()
qr.show()
time.sleep(15)
list_of_message = [{'contact': 'Test','message':'Hello There!'}, {'contact': 'Test','message':'How are you?'},{'contact': 'Test','message':'mmmh?'}]

for message in list_of_message:
    queue.create_message(**message)

queue.start_worker()