from mongoengine import *

#1. design database
class Service(Document):
  name = StringField()
  yob = IntField()
  gender = IntField()
  height = IntField()
  phone = StringField()
  address = StringField()
  status = BooleanField()
  description = ListField()
  measurement = ListField()
  img = StringField()

