from whatsapp.driver_class import WhatsappMessaging
from flask import jsonify

def user_logged_in(function_call):    
    def wrapper(*args, **kwargs):
        driver = WhatsappMessaging()
        if driver.logged_in:
            return function_call(*args, **kwargs)
        elif driver.check_if_user_logged_in():
            return function_call(*args, **kwargs)
        else :
            return jsonify({"success": False, "error":"user not logged in"}), 400
    return wrapper