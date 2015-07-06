#encoding: utf-8
from peewee import *

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "123456"
DB = "test"
PORT = 3306

peeweeDb = MySQLDatabase(DB, user=USER,passwd=PASSWORD)
class DmozItem(Model):
    title = CharField()
    link = CharField()
    desc = TextField()
    class Meta:
        database = peeweeDb

peeweeDb.connect()
DmozItem.create_table(True)
