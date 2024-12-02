from pydantic import BaseModel, BeforeValidator, Field, AliasChoices
from typing import Annotated, Optional


class Address(BaseModel):
    city: Annotated[str, Field(min_length=1)]
    country: Annotated[str, Field(min_length=1)]


class Student(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    age: Annotated[int, Field(gt=0, lte=100)]
    address: Address


class StudentInfo(Student):
    id: Annotated[str, BeforeValidator(str)] = Field(validation_alias=AliasChoices("_id", "id"))


class AddressUpdateInfo(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class StudentUpdateInfo(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[AddressUpdateInfo] = None
