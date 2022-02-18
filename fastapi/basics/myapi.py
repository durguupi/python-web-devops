from sys import int_info
from turtle import st
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# Instance of FastAPI
app = FastAPI()

students = {
    1: {
        "name": "John",
        "age" : 17,
        "year": "year12"   
    },
    2: {
        "name": "David",
        "age" : 16,
        "year": "year11"   
    }
}
# Class Model for student
class Student(BaseModel):
    name: str
    age: int
    year: str
# created a new class model for update student since we need all paramters that needs to be passed for PUT should
# be optional 
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# /docs creates FastAPI UI where we can test our endpoint like how we test in PostMan
# GET request to root page /
@app.get("/")
def index():
    return {"Name": "First data"}

# PATH PARAMETERS: Endpoint now its hitting is /student/id , id ==> Will be dynamic based on input of user
# Description displays message in /docs UI when testing as what is to be passed in student_id
# http://127.0.0.1:8000/student/1
@app.get("/student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view")):
    return students[student_id]


# Query parameter ==> http://127.0.0.1:8000/byname?name=John
@app.get("/byname")
def get_student_name(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}


# POST REQUEST stduentk (key) is assigend to value of Student class which will create new student object 
# It asks for value of name,age and year then creates student of ID which we gave
@app.post("/create-student/{student_id}")
def create_student(student_id: int, studentk: Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    students[student_id] = studentk
    return students[student_id]

# PUT Method ==> Update data that already exists
# Updates only when value is not none if its not given then it will keep old data
@app.put("/update-student/{student_id}")
def update_student(student_id: int, studentk: UpdateStudent):
    if student_id not in students:
        return{"Error": "Student does not exist"}
    
    if studentk.name != None:
        students[student_id].name = studentk.name

    if studentk.age != None:
        students[student_id].age = studentk.age

    if studentk.year != None:
        students[student_id].year = studentk.year  
    
    return students[student_id]

# DELETE METHOD ==> http://127.0.0.1:8000/delete-student/3
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int ):
    if student_id not in students:
        return {"Error": "Student Does not Exist"}
    del students[student_id]
    return {"Message": f"Student of ID {student_id} is deleted successfully "}