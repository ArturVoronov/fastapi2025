from pydantic import BaseModel

class Todo(BaseModel):
    todo:str
    description:str
