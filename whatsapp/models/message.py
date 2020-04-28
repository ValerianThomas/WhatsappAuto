from datetime import datetime
from pymodm import MongoModel, fields

class Message(MongoModel):
    contact = fields.CharField(required=True)
    message = fields.CharField(required=True)
