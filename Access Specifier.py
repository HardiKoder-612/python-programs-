"""Rules are same as in java"""
#public: write the data member normally
#protected: Write the data member with starting with (_) underscore
#Private: Write the data memebr with starting with double (__) underscore
class Employee:
    no_of_leaves=8
    public =6
    _protec=9               #Protected variable
    __priv=10               #Private variable
    def __init__(self, aname, asalary, arole):  # __init__() is the constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetail(self):
        return f"The name is {self.name}\nAnd the number is {self.num}\nAnd the list is {self.l}\n the number of the class variable is {Employee.num}"

    def printprivate(self):
        print(self.__priv)

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

obj=Employee("Hardik",10000,"Student")
karan=Programmer("Karan",21,"Programmer",["Python"])
print(obj.public)
print(obj._protec)
obj.printprivate()      #to print private variable
"""OR"""
print(obj._Employee__priv)          # To print private variable without any member function

print(karan.public)
print(karan._protec)            #We can access protected members of inherited class
#print(karan.__private)         #We cannot access private variables using derived class
#print(karan._Employee__priv)   #We cannot access private variables using derived class
