a = 9
b = 8
c = sum((a, b))  # Pre-defined function


def func1():  # nuser deined function declaration and definition
    print("This is function 1")


v = func1()  # func1 calling
print(v)  # prints none because func1 does not return any value


def func2(a, b):
    print("Sum of ", a, " and ", b, " is: ", a + b)


func2(10, 12)


def func3(a, b):
    """This is a function which will return the average of two numbers."""              #doc string i.e. first line of every function when written inside 3 double quotes
    average = (a + b) / 2
    return average


q = func3(10,12)
print("The average of both numbers is ", q)
print(func3.__doc__)        #It will print the doc-string of the function 3
print(func2.__doc__)        # It will print none because func2 does not have any doc-string associatedd with it.
