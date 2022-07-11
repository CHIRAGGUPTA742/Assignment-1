class Student:
    pass
class Marks:
    pass
Chirag=Student()
a_grade=Marks()
print("To check whether they are instances of said classes or not:")
print(isinstance(Chirag,Student))
print(isinstance(Chirag,Marks))
print(isinstance(a_grade,Marks))
print(isinstance(a_grade,Student))
print("\nTo check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(Student,object))
print(issubclass(Marks,object))
