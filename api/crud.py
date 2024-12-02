from typing import Any, Dict, List, Optional

from bson import ObjectId
from . import schemas
from .database import students_collection


async def register_student(student: schemas.Student) -> schemas.StudentInfo | None:
    student_data = student.model_dump()
    result = await students_collection.insert_one(student_data)
    created_student = await students_collection.find_one({"_id": result.inserted_id})
    if created_student:
        return schemas.StudentInfo(**created_student)
    return None



async def fetch_all_students(age: Optional[int] = None, country: Optional[str] = None) -> List[Dict[str, Any]]:
    query = {}

    if country:
        query["address.country"] = country
    
    if age is not None:
        query["age"] = {"$gte": age}

    students_cursor = students_collection.find(query)
    return await students_cursor.to_list(length=100)  # Convert the cursor to a list


async def fetch_one_student(id: str) -> schemas.StudentInfo | None:
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student:
        return schemas.StudentInfo(**student)
    return None


async def update_student(id: str, info: schemas.StudentUpdateInfo) -> schemas.Student | None:
    required_updates = info.model_dump(exclude_none=True)
    # print(required_updates)

    result = await students_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": required_updates}
    )
    if result.matched_count == 0:
        return None

    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student:
        return schemas.StudentInfo(**student)
    return None
   

async def delete_student(id: str) -> bool:
    result = await students_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count != 0
