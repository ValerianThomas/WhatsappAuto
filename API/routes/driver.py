import os
import json 
from flask import jsonify, Blueprint
from whatsapp.driver_class import WhatsappMessaging



driver_api = Blueprint('driver_api',__name__)

@driver_api.route('/',methods=['GET'])
def login_driver():
    driver = WhatsappMessaging()
    qr_code = driver.get_login_qr_code()
    # TODO: for now we are just showing the qr code but later on we must save it a temp folder and show it in the front end, then delete it when login is done.
    # TODO: detect when a login is successful or not.
    qr_code.show()
    return jsonify({"success":True}), 200