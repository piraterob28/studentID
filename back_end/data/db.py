#db.py
import sqlite3
from sqlite3 import Error
from contextlib import closing
from data.models import Student
from . import DB_PATH


def get_conn():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def get_students():
    connection = get_conn()
    cursor = connection.cursor()
    row = cursor.execute("SELECT Student, Student_ID, Housing, Department, Year FROM students").fetchall()
    connection.close()
    return row

def add_student(student: Student):
    connection = get_conn()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO students VALUES (?,?,?,?,?)", (student.studentid, student.studentname, student.building, student.department, student.year))
    connection.commit()
