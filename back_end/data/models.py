
from pydantic import BaseModel

class Student(BaseModel):
    studentid: str
    studentname: str
    building: str
    department: str
    year: str