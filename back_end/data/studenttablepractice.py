#studenttablepractice.py
import sqlite3
from sqlite3 import Error
from contextlib import closing

def create_connection(db_file):
    """create a database connection to a SQLite database"""
    connection = None

    try:
        connection =sqlite3.connect(db_file)
        cursor = connection.cursor()
        # cursor.execute("CREATE TABLE students(Student_ID TEXT PRIMARY KEY, Student TEXT, Housing TEXT, Department TEXT, Year TEXT)")
        # cursor.execute("INSERT INTO students VALUES('00001', 'Billy Jean', 'Crypts', 'Mastery of Blurry Photos', 'Apprentice')")
        # cursor.execute("INSERT INTO students VALUES('00069', 'Darius Houle', 'Your Moms House', 'Black Magic Fuckery', 'Grand Master Wizard')")
        connection.commit()
        rows = cursor.execute("SELECT Student, Student_ID, Housing, Department, Year FROM students").fetchall()
        print(rows)

    except Error as e:
        print(e)

    finally:

        with closing(sqlite3.connect("pythonsqlite.db")) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute("SELECT 1").fetchall()
                print(rows)


create_connection(r"C:\Users\rober\CodingProjects\WebDevIntro\Student_ID\back_end\data\pythonsqlite.db")
