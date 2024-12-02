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
    city: Optional[Annotated[str, Field(min_length=1)]] = None
    country: Optional[Annotated[str, Field(min_length=1)]] = None

class StudentUpdateInfo(BaseModel):
    name: Optional[Annotated[str, Field(min_length=1)]] = None
    age: Optional[Annotated[int, Field(gt=0, lte=100)]] = None
    address: Optional[AddressUpdateInfo] = None
