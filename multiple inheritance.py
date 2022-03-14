class Employee:
    no_of_leaves=8
    var=5
    def __init__(self, aname, asalary, arole):  # __init__() is the constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetail(self):
        return f"The name is {self.name}\nAnd the salary is {self.salary}\nAnd the role is {self.role}\n the number of the class variable is {Employee.no_of_leaves}"

    @staticmethod
    def printgood(str):
        print(f"This is a good {str}")
        return "Thenga"
    pass

class Player:
    no_of_Games=4
    var=10
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"The name is {self.name}\nAnd game is {self.game}"
    pass

class CoolProgrammer(Employee,Player):              #Order is important
    langauge="C++"
    def printlangauge(self):
        print(self.langauge)
    pass

harry=Employee("haryy",12,"Student")
hardik=Employee("hardik",10,"Instructor")
shubham=Player("Hardik",["Cricket"])
karan=CoolProgrammer("Karan",899,"CoolProgrammer")
det=karan.printdetail()
print(det)
karan.printlangauge()
print(karan.var)                    #First of all it will prnit var of its own class if it is there
                                    #If it is not there then it will check the parent class in order specified in inheritance
                                    #i.e. check inside brackets, those class whose name is first it will check that class
                                    #If the variable is found in that class then it will print that value
                                    # If not find in that class then check next class of the brackets
                                    