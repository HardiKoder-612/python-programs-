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

harry=Employee("haryy",12,"Student")
hardik=Employee("hardik",10,"Instructor")
# """CLASS METHOD"""
# harry.change_leaves(89)
# print(Employee.no_of_leaves)

print(hardik.printgood("Hardik"))