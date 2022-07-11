def student_data(student_id,**kwargs):
    print("Student ID:",student_id)
    if "student_name" in kwargs:
        print("Student name :",kwargs['student_name'])
    if "student_class" in kwargs :
        print("Student class :",kwargs['student_class'])
        

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')

student_data(student_id='SV12', student_name='Jean Garner')
