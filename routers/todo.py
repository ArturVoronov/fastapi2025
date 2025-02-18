from fastapi import APIRouter
from model.pydentic_model import Todo
import all_routers
import operations.to_do as db


todo_router = APIRouter()

#create a new todo
@todo_router.post(all_routers.todo_create)
def new_todo(doc:Todo):
    doc = dict(doc)
    todo: str = doc['todo']
    res = db.create_to_do(todo)
    print(res)
    return res

@todo_router.get(all_routers.todo_all)
def all_todos():
    res = db.get_all()
    return res 

@todo_router.get(all_routers.todo_one)
def one_todo(_id:int):
    res = db.get_one(_id)
    return res 

#update one
@todo_router.patch(all_routers.todo_update)
def update_todo(_id:int, doc: Todo):
    doc = dict(doc)
    title :str = doc['todo']
    res = db.update_todo(_id, title)
    return res 

@todo_router.delete(all_routers.todo_delete)
def delete_todo(_id:int):
    res = db.delete_todo(_id)
    return res 
