from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

# Create and Retrieve
# Start here

# Scenario: A university needs an API to register students and retrieve their records. It doesn't have a database yet, so you're temporarily using a Python list.
# Requirements
# Build one FastAPI application with the following behavior:
# Method	Endpoint	Required behavior
# POST	/students	Register a student and save the record in memory
# GET	/students	Return all currently registered students
# GET	/students/{student_id}	Retrieve one student using their ID
# Each student must have a name, age, and unique numeric id.
# The client should provide the name and age. Your application should assign the ID automatically.
# Use a Pydantic model for request validation.


class Students(BaseModel):
    name:str
    age:int
    department:str
    Id:int

data=[]

@app.post("/students",status_code=201)
def test(student:Students):
    if (student.age<=0 or student.Id<=0) :
        raise HTTPException(
            status_code=400,
            detail=f"Bad request , error: 400"

        )
    else:
        data.append({
            "Name":student.name,
            "Age":student.age,
            "Department":student.department,
            "Id":student.Id
        })

    return f"Data saved successfully: {data}"



@app.get("/students")
def test():
    return data



@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in data:
        if student["Id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )