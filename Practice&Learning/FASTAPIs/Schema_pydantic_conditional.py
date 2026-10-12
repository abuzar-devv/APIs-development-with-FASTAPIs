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