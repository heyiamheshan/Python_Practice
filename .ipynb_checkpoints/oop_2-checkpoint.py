class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Student created: "+self.name+","+str(self.age))

student1=Student("John",20)
student2=Student("Jane",25)