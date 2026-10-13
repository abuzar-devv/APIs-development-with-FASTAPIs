# Practice 1 — Validate a person's age
# Age validation API
# Beginner

# Scenario: You're building an API that accepts a person's name and age.
# Requirements
# - Create a Person Pydantic model with name as text and age as an integer.
# - Create a POST /people endpoint.
# - If age is below zero, return HTTP 422 with a helpful error message.
# - Otherwise, return the person's name and age as JSON.
# - Don't use advanced Pydantic validation features yet.

from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app=FastAPI()

class Data(BaseModel):
    name:str
    age:int

@app.post("/people")
def test(validation:Data):
    if validation.age<0:
        raise HTTPException(
            status_code=422,
            detail="Age cannot be -ve"
        )

    return {
        "Name":validation.name,
        "Age":validation.age
    }


#Task 2

# Goal: Build an API for a university that accepts student registrations and provides a way to retrieve student information.
# You already implemented POST /students and successfully tested registration in Postman. You also encountered a 405 Method Not Allowed when opening /students in Chrome.
# Your next task
# Implement GET /students while preserving your existing POST /students endpoint.
# Requirements:
# - POST /students must continue accepting student data: name, age, and program.
# - GET /students must respond to a GET request.
# - Test both endpoints in Postman.
# - Explain why Chrome produced 405 previously and why adding a GET endpoint changes that behavior.

class Students(BaseModel):
    name:str
    age:int
    program:str

@app.post("/students")
def test(student:Students):
    if student.age<0:
        raise HTTPException(
            status_code=422,
            detail="Age cannot be -ve , validation failed"
        )

    return{
        "Name":student.name,
        "Age":student.age,
        "Program":student.program
    }

@app.get("/students")
def test():
    return {
        "Name":"Abu zar",
        "Age":20
    }