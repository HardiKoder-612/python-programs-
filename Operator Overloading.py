class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):  # __init__() is the constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"The name is {self.name}\nAnd the number is {self.num}\nAnd the list is {self.l}\n the number of the class variable is {Employee.num}"

    @classmethod
    def change_leaves(cls, leaves):  # cls is that class which owns the instance which is used to call this method
        cls.no_of_leaves = leaves

    def __add__(self, other):                           #self is object first and other is object second
        return self.salary+other.salary



emp1=Employee("Hardik",6000,"Programmer")
emp2=Employee("Rohan",60,"Cleaner")

print(emp1+emp2)