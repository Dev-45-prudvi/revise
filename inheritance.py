from myclass import Student
class Student1(Student):
    def __init__(self,name,age,rollnum,department,isSuspended,cgpa):
        super().__init__(name, age, rollnum, department, isSuspended)
        self.cgpa = cgpa
