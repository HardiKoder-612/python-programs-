class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):  # __init__() is the constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetail(self):
        return f"The name is {self.name}\nAnd the number is {self.num}\nAnd the list is {self.l}\n the number of the class variable is {Employee.num}"

    @classmethod
    def change_leaves(cls,leaves):                     #cls is that class which owns the instance which is used to call this method
        cls.no_of_leaves=leaves
    @classmethod
    def class_str(cls,str):
        params=str.split("-")
        print(params)
        return cls(params[0],params[1],params[2])
    """OR WE can do above three in folllowing one line
        return cls(*str.split("-))
    """
    pass

harry=Employee("haryy",12,"Student")
hardik=Employee("hardik",10,"Instructor")
rohan=Employee.class_str("Rohan-12-Student")
# """CLASS METHOD"""
# harry.change_leaves(89)
# print(Employee.no_of_leaves)
print(rohan.no_of_leaves)