def simple_table():
    print("Printing table using simple function.")
    num=int(input("Enter the number whose table is to be printed: "))
    for i in range(2,21):
        print(f"{num} * {i} = {num*i}")
simple_table()
print("\n\n")


def param_table(num):
    for i in range(2, 21):
        print(f"{num} * {i} = {num * i}")

print("Printing table using parameterized function is: ")
num = int(input("Enter the number whose table is to be printed: "))
param_table(num)
print("\n\n")
