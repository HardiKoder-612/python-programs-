def factorial(n):
    if(n==1):
        return 1
    fact=n*factorial(n-1)
    return fact

num=int(input("Enter the number whose factorial is to be calculated: "))
result=factorial(num)
print("Factorial of the number is: ",result)