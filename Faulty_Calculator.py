# 45*3=555,  56+9 = 77, 56/6 =4
var1 = int(input("Enter number 1: "))
var2 = int(input("Enter number 2: "))
var3 = input("Enter operator to be used(/,*,+,-): ")
if var3 == "/":
    if var1 == 56 and var2 == 6:
        print(var1, "/", var2, "= 4")
    else:
        print(var1, "/", var2, "=", var1 / var2)
elif var3 == "*":
    if (var1 == 45 and var2 == 3) or (var1 == 3 and var2 == 45):
        print(var1, "*", var2, "=555")
    else:
        print(var1, "*", var2, "=", var1 * var2)
elif var3 == "+":
    if (var1 == 56 and var2 == 9) or (var1 == 9 and var2 == 56):
        print(var1, "+", var2, " = 4")
    else:
        print(var1, "+", var2, "=", var1 + var2)
