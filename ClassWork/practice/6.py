#6. Python program to demonstrate variables scope
y=20
def method():
    x=10
    print(x,y)
method()
print(y)
print(x)