#main.py

from typing import Optional 
from fastapi import FastAPI
from data.db import get_students, add_student
from data.models import Student
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students")
def student_table():
    return get_students()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/students")
async def new_student(student: Student):
    print(student)
    add_student(student)
    return student
