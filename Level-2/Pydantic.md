## Pydantic is a Python library for defining the structure of data and validating that data using Python type hints.


BaseModel is a class provided by Pydantic that you inherit from to create your own data model.


BaseModel → creates the model
Type hints → define the data type
Field() → adds validation rules

Field() is used inside a Pydantic model to add extra rules, validation, and metadata to a field.
Think of it like:
Type hint = basic rule
Field() = additional rules


## 1. Normal BaseModel — most common
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int


## 2. Model with default values
class Student(BaseModel):    name: str    age: int = 18


Here, age is optional because it has a default value.


## 3. Model with validation constraints
You can use Field() to add restrictions.
from pydantic import BaseModel, Fieldclass Student(BaseModel):    name: str = Field(min_length=3)    age: int = Field(ge=18, le=60)


Here:
- min_length=3 → name must have at least 3 characters
- ge=18 → age must be ≥ 18
- le=60 → age must be ≤ 60


## 4. Nested models
One Pydantic model can be used inside another.
class Address(BaseModel):    city: str    pincode: intclass Student(BaseModel):    name: str    address: Address


Example:


student = Student(
    name="Saloni",
    address={
        "city": "Indore",
        "pincode": 452001
    }
)



| Parameter | Meaning | Example |
|---|---|---|
| `default` | Default value | `Field(default=20)` |
| `min_length` | Minimum string length | `Field(min_length=3)` |
| `max_length` | Maximum string length | `Field(max_length=100)` |
| `ge` | Greater than or equal to | `Field(ge=18)` |
| `le` | Less than or equal to | `Field(le=100)` |
| `gt` | Greater than | `Field(gt=0)` |
| `lt` | Less than | `Field(lt=100)` |
| `description` | Describes the field | `Field(description="Student age")` |