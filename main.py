from routers.todo import todo_router
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import operations.to_do as db
from model.pydentic_model import Todo
from connection import db_session

app = FastAPI()

app.include_router(todo_router)
templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory='static'), name='static')
  
@app.get('/')
def index(req:Request):
    return templates.TemplateResponse(
        name='index.html',
        context={'request':req}
    )
@app.get('/index/', response_class=HTMLResponse)
def index1(request:Request):
    films=[
        {'name':'Blade Runner', 'director':'Ridley Scott'},
        {'name':'Pulp Fiction', 'director':'Quentin Tarantino'},
        {'name':'Mulholland drive', 'director':'David Lynch'},
    ]
    context = {'request': request, 'films':films}
    return templates.TemplateResponse("index.html", context)
@app.get('/database/', response_class=HTMLResponse)
def index2(request:Request):
    res = db.get_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index1.html", context)

from fastapi.responses import FileResponse
 

@app.get('/database/{_id}', response_class=HTMLResponse)
def index4(request:Request, _id):
    db.delete_todo(_id)
    res = db.get_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index1.html", context) 

@app.get('/forma/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse('forma.html', {'request': request})

@app.post('/disable')
async def disable_cat(request: Request, cat_name: str = Form(...), Description: str = Form(...)):
  
    db.create_to_do(cat_name, Description)
    res = db.get_all()
    context = {'request': request, 'res':res}
    return templates.TemplateResponse("index1.html", context)

   # return f'{cat_name} category has been disabled.',{"todo":cat_name, "description":Description}


if __name__=="__main__":
    uvicorn.run("main:app", reload=True)
