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
    pass

harry=Employee("haryy",12,"Student")
hardik=Employee("hardik",10,"Instructor")
print(Employee.no_of_leaves)
print(hardik.no_of_leaves)

hardik.no_of_leaves=10
print(Employee.no_of_leaves)            #It will print 8 because the value through instance hardik has been changed not the default value

"""Special  case"""
#In this when we print value of variable using class name then it will print 9 because we have changed it through line 25
#But value through hardik object will be 10 as in line 20
"""To prevent this type of complexity we use classmethod decorator"""
Employee.no_of_leaves=9
print(hardik.no_of_leaves)
print(Employee.no_of_leaves)


"""CLASS METHOD"""
hardik.change_leaves(89)
print(Employee.no_of_leaves)