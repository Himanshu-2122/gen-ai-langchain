from typing import TypedDict



class Person (TypedDict):

    name : str
    age : int


p1 : Person = {"name":"himanshu" ,   "age":24}

print (p1)