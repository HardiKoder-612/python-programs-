#This program prints the value at an index n of the series 0 1 1 2 3 5 ........
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("\nEnter the range: "))
print(fibonacci(num))

