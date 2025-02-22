from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import datetime

def get_timestamp():
    return datetime.datetime.now()

BASE = declarative_base()

#creating our model or table
class Todo(BASE):
    __tablename__:str ='to_do'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)
    timestamp = Column (DateTime, default=get_timestamp())
    description = Column(String)
    def __init__(self, todo, description):
        self.todo = todo
        self.description = description
        

