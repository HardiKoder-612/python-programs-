num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
try:
    num3=num1/num2
    print(num3)
except Exception as e:
    print(e)
    print("Divide by zero exception")

print("This line is very important")