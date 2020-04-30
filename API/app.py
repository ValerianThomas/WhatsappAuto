import logging
from flask import Flask, request, jsonify
from API.routes.driver import driver_api
from API.routes.messager import message_api
from API.config import app_config

#------- Basic setup -------
# remove keras cach and initialize logger
logging.basicConfig(format='%(asctime)s %(message)s')


def create_app ():
  app = Flask(__name__)
  app.config.from_object(app_config['development'])
  app.register_blueprint(driver_api, url_prefix='/driver')
  app.register_blueprint(message_api, url_prefix='/message')
  @app.route('/ping',methods=['GET'])
  def is_server_running():
    return 'server running'

  return app