# Simple Task API

A simple REST API built with FastAPI for teaching purposes. This API demonstrates basic CRUD operations for managing tasks.

## Features

- Create, Read, Update, and Delete tasks
- In-memory storage
- Automatic API documentation
- Docker support

## Running the API

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

### Using Docker

1. Build the Docker image:
```bash
docker build -t task-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 task-api
```

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation: http://localhost:8000/docs
- ReDoc documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Welcome message
- `GET /tasks` - Get all tasks
- `GET /tasks/{task_id}` - Get a specific task
- `POST /tasks` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## Example Task JSON

```json
{
    "title": "Learn FastAPI",
    "description": "Study FastAPI documentation",
    "completed": false
}
``` 