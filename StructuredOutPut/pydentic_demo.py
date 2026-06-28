from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int]
    year: int
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description="A decimal value representing the cgpa of the student")

new_student = {'name': 'trupti', 'age': '33', 'year':2026, 'email': 'trupti.wanpal@gmail.com', 'cgpa' : '9'}
student = Student(**new_student)


print(student)

print(student.name)

print(student.age)

print(student.year)

print(student.email) #error if not valid email

print(student.cgpa) #error if value is greater than or equal to 10

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()

print(student_json)