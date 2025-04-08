from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="Task API", description="A simple REST API for teaching purposes")

# In-memory storage
tasks = []

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    completed: bool = False

@app.get("/")
async def root():
    return {"message": "Welcome to the DIEGO API!"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    task.id = str(uuid.uuid4())
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated_task.id = task_id
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found") 