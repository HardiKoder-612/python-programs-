age=int(input("Enter your age: "))
if(age>=7 and age<90):
    if(age>18):
        print("You can drive")
    elif(age==18):
        print("Please come to our office to get verified")
    else:
        print("You cannot drive")
else:
    print("Enter a valid age")