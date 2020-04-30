import os
import json 
from flask import request, jsonify, Blueprint
from whatsapp.queue_class import MessageQueue
from utils.decorators import user_logged_in


message_api = Blueprint('message_api',__name__)


@message_api.route('/',methods=['POST'])
@user_logged_in
def new_message():
    data = request.get_json()
    if not 'contact' in data :
        return jsonify({"success":False, "error": "missing contact in request"}), 400
    if not 'message' in data :
        return jsonify({"success":False, "error": "missing message in request"}), 400
       # TODO: continue with the message  creation
    messageQueue = MessageQueue()
    messageQueue.start_worker()
    messageQueue.create_message(data['contact'], data['message'])
    return jsonify({"success":True, "error": "message sent to the queue"}), 200

