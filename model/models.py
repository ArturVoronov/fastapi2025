from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, DateTime, MetaData
import datetime


def get_timestamp():
    return datetime.datetime.now()

class Base(DeclarativeBase):
    metadata = MetaData()

#creating our model or table
class Todo(Base):
    __tablename__:str ='to_do'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)
    timestamp = Column (DateTime, default=get_timestamp())
    def __init__(self, todo):
        self.todo = todo

