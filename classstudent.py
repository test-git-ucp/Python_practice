class student:
    def __init__(self,studentname,age,rollno,clas,marks):
        self.studentname=studentname
        self.age=age
        self.rollno=rollno
        self.clas=clas
        self.marks=marks
    def update(self,updatemark):
        self.marks=updatemark
        print(f"the marks is updated {self.marks} ")   
    def pas(self):
        if self.marks >50:
            print("pass/fail=pass")
        else:
            print("pass/fail=fail")
    def check_info(self):
        print(f"student name :{self.studentname}")
        print(f"student Age :{self.age}")
        print(f"student rollno :{self.rollno}")
        print(f"student class :{self.clas}")
        print(f"student marks :{self.marks}")
        
acc=student("Ali",23,"17",10,73)
acc.check_info()
acc.update(55)
acc.pas()