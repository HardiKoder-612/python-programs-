class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):  # __init__() is the constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetail(self):
        return f"The name is {self.name}\nAnd the number is {self.num}\nAnd the list is {self.l}\n the number of the class variable is {Employee.num}"

    @staticmethod
    def printgood(str):
        print(f"This is a good {str}")
        return "Thenga"
    pass

class Programmer(Employee):                 #"""SINGLE INHERITANCE"""
    def __init__(self,name,age,role,language):
        self.name=name
        self.age = age
        self.role = role
        self.language = language
    def printprog(self):
        return f"The name of the person is {self.name}, age is {self.age}, role is {self.role} and language he knows is {self.language}"
    pass

harry=Employee("haryy",12,"Student")
hardik=Employee("hardik",10,"Instructor")
karan=Programmer("Karan",21,"Programmer",["Python"])
shubham=Programmer("Shubham",22,"Student",["Python","Java"])

print(karan.printprog())
print(karan.no_of_leaves)
