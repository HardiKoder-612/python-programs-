str1=input("Enter the string 1: ")
str2=input("Enter the string 2: ")
for i in str1.split( ):
    if i not in str2.split( ):
        print(i,end=", ")
for i in str2:
    if i not in str1:
        print(i,end=", ")