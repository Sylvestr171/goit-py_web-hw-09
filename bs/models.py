from mongoengine import Document, ReferenceField
from mongoengine.fields import DateTimeField, StringField, ListField
from datetime import datetime
from connect import connect

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)
    created = DateTimeField(default=datetime.now(), required=True)

class Quotes (Document):
    tags = ListField()
    author = ReferenceField(Authors, required=True)
    quote = StringField(required=True)
    created = DateTimeField(default=datetime.now(), required=True)