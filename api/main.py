from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from bson.errors import InvalidId

from . import crud
from . import schemas


app = FastAPI()



@app.post("/students", response_model=schemas.StudentInfo, status_code=status.HTTP_201_CREATED)
async def create_student(student: schemas.Student):
    student = await crud.register_student(student)
    if student is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
    return student


@app.get("/students", response_model= List[schemas.StudentInfo],status_code=status.HTTP_200_OK)
async def fetch_all_students(age: Optional[int] = None, country: Optional[str] = None):
    return await crud.fetch_all_students(age, country)


@app.get("/students/{id}", response_model=schemas.StudentInfo, status_code=status.HTTP_200_OK)
async def fetch_student(id: str):
    try:
        student = await crud.fetch_one_student(id)
    except InvalidId:
        student = None

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.patch("/students/{id}", response_model=schemas.StudentInfo, status_code=status.HTTP_200_OK)
async def update_student(id: str, info: schemas.StudentUpdateInfo):
    try:
        student = await crud.update_student(id, info)
    except InvalidId:
        student = None
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
       

@app.delete("/students/{id}", status_code=status.HTTP_200_OK)
async def delete_student(id: str):
    try:
        success = await crud.delete_student(id)
    except InvalidId:
        success = False
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return {"detail": "student deleted"}
    
