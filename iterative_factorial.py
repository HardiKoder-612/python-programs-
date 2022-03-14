#recursion is when a function calls itself
def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

num=int(input("Enter the number whose factorial is to be calculated: "))
result=factorial(num)
print("Factorial of the number is: ",result)