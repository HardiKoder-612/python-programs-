class A:
    classvar1="I am in class A variable"
    def __init__(self):
        self.var1="I'm in constructor of class A"
        self.classvar1="Instance variable in class A"
        self.special="Special"
    pass


class B(A):
    classvar2="I am in class varibale of B"
    def __init__(self):
        self.var1="I'm in constructor of class B"
        self.classvar1="Instance variable in class B"
        super().__init__()                                  #It will override the constructor of inherited class
    pass

a=A()
b=B()
print(b.classvar1)
#print(b.special)                #If we don't write super, it will give error beccause the constructor of base class has been overrided
print(b.special,b.var1,b.classvar1)
