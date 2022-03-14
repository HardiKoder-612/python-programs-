#Classes-template
#Object=Instance of the class

class Student:
    num=21

    def printdetail(self):
        return f"The name is {self.name}\nAnd the number is {self.num}\nAnd the list is {self.l}\n the number of the class variable is {Student.num}"

    """self will be that object which is used to call this function"""
    pass


obj1 = Student()  # obj1 is the object of class Student
obj1.name = "Hardik"
obj1.num = 10
obj1.l = ["Hardik", "Sharma"]
print(obj1.printdetail())
print(obj1.name)
print(obj1.num)
print(obj1.l)
print(Student.num)      #Will print num variable of the class
obj2=Student()
obj2.num=22         #This will not change the variable num of the class, it will create another reference of obj2 which will have variable num
print(Student.num)
print(obj2.num)