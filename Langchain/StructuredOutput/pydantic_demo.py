from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name:str="userr"
    age:Optional[int]=None
    email:EmailStr="user@gmail.com"
    cgpa: float = Field(gt=0,lt=10,default=7,description='the cgps score of student out of 10')
new_student={'name':'janvi','cgpa':9.5}
student=Student(**new_student)
# print(student)
student_dict=dict(student)
print(student_dict['cgpa'])