# #Enhance the functionality of functions
# def func1():
#     print("Hello")
# func2=func1         #copy all the details of func1 in func2
# del func1           # If we delete the func1() then also func2 will run
# func2()

##################FUNCTION RETURNING FUNCTION############################

def funcret(num):
    if num==0:
        return print
    else:
        return int
a=funcret(0)
b=funcret(1)
print(a,b)

####################Passing function as an argument######################
def funcpass(func):
    func("This is function")

funcpass(print)

"""################################ DECORATORS ##################################"""
def dec1(func1):
    def nowexec():
        print("Executing Now....")
        func1()
        print("Executed")
    return nowexec()

@dec1                               #This means that hardik() function is a decorator of dec1()
#                                         We can also write it as
#                                         hardik()=dec1(hardik())
#
def hardik():
    print("Hardik is a good boy")

hardik()