from pydantic import BaseModel , EmailStr , Field
class Student (BaseModel):

    name : str 

    email : EmailStr

    cgpa : float = Field(gt = 0 , lt = 10 )




student = Student (name = "himanshu" , email = "himanshu@example.com" , cgpa =  8.34)
print(student)