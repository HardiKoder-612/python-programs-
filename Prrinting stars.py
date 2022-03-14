n = int(input("Enter the number: "))
b = int(input("Enter the boolean: "))
new=bool(b)
if b:
    for i in range(n + 1):
        for j in range(i):
            print("*", end="")
        print("")

else:
    for i in reversed(range(n + 1)):
        for j in range(i):
            print("*", end="")
        print("")
