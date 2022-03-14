# *args is Just like varags in java
#But arguments will be passed as a tupple
def funargs(*args):
    print(args[0])

har=["hardik","Ram","Mohan","Rohan"]
funargs(*har)

def printargs(*argslist):
    print(*argslist)

dhar=["Hardik","Sham","Rohan","Sohan","Mohan"]
printargs(*dhar)

"""kwargs is used for passing dictionary like lists"""
#example

def printdiction(normal,*args,**kwargs):                #*args and ** kwargs are optional but normal argument is mandatory
    print(normal)
    print(args)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

dic={"Hardik":"Programmer","Momos":"Junk food","Levi":"Ackerman","Erwin":"Smith"}
printdiction(har,*dhar,**dic)
printdiction(har)