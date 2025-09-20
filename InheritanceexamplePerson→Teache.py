class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def persona(self):
        print(f"name={self.name}")
        print(f"age={self.age}")
        
class teacher(person):
   def __init__(self, name, age,subject ,salary):
       super().__init__(name, age) 
       self.subject=subject
       self.salary=salary
   def tech(self):
       print(f"name={self.name}")
       print(f"age={self.age}")
       print(f"subject={self.subject}")
       print(f"salary={self.salary}")
t1=teacher("Ali",34,"Math",100000)
t1.tech()