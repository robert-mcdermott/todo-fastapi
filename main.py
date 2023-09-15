
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: Optional[bool] = False

@app.get('/todos')
def get_todos():
    return todos

@app.post('/todos')
def add_todo(todo: Todo):
    todos.append(todo.dict())
    return {'message': 'Todo added successfully!'}

@app.delete('/todos/{id}')
def delete_todo(id: int):
    global todos
    todos = [todo for todo in todos if todo['id'] != id]
    return {'message': 'Todo deleted successfully!'}
