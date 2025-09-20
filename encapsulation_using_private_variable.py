class stdent:
    def __init__(self,name,age,marks):
        self.__name =name
        self.__marks =marks
        self.__age =age
    def get_name(self):
        return self.__age
        return self.__name
    
t1=stdent("Ali",42,45)
print(t1.self.name)#we cannot recall private variable directlly
print(t1._stdent__name)
print(t1._stdent__age)