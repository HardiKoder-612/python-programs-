name = input("Enter name: ")
c = int(input("What do you want to do?\n1. enter data\n2. retrieve data\n->"))
def getdate():
    import datetime
    return datetime.datetime.now()
if c == 1:
    if name == "Hardik":
        fe = open("hardikex.txt", "a")
        fd = open("hardikdiet.txt", "a")
        dat = str(getdate())
        choice = int(input("1. For diet entry\n2. For exercise entry\n->"))
        if choice == 1:
            food = input("Enter the food you eat: ")
            fd.write("\n[")
            fd.write(dat)
            fd.write("]\n")
            fd.write(food)
        elif choice == 2:
            exercise = input("Enter the exercise you have done: ")
            fe.write("\n[")
            fe.write(dat)
            fe.write("]\n")
            fe.write(exercise)
        fe.close()
        fd.close()
    elif name == "Ram":
        fe = open("ramex.txt", "a")
        fd = open("ramdiet.txt", "a")
        dat = str(getdate())
        choice = int(input("1. For diet entry\n2. For exercise entry\n->"))
        if choice == 1:
            food = input("Enter the food you eat: ")
            fd.write("\n[")
            fd.write(dat)
            fd.write("]\n")
            fd.write(food)
        elif choice == 2:
            exercise = input("Enter the exercise you have done: ")
            fe.write("\n[")
            fe.write(dat)
            fe.write("]\n")
            fe.write(exercise)
        fe.close()
        fd.close()
    elif name == "Rohan":
        fe = open("rohanex.txt", "a")
        fd = open("rohandiet.txt", "a")
        dat = str(getdate())
        choice = int(input("1. For diet entry\n2. For exercise entry\n->"))
        if choice == 1:
            food = input("Enter the food you eat: ")
            fd.write("\n[")
            fd.write(dat)
            fd.write("]\n")
            fd.write(food)
        elif choice == 2:
            exercise = input("Enter the exercise you have done: ")
            fe.write("\n[")
            fe.write(dat)
            fe.write("]\n")
            fe.write(exercise)
        fe.close()
        fd.close()
elif c == 2:
    if name == "Hardik":
        fe = open("hardikex.txt")
        fd = open("hardikdiet.txt")
        choice = int(input("1. For diet\n2. For exercise\n->"))
        if choice == 1:
            print(fd.read())
        elif choice == 2:
            print(fe.read())
    if name == "Ram":
        fe = open("ramex.txt", "r")
        fd = open("ramdiet.txt", "r")
        choice = int(input("1. For diet\n2. For exercise\n->"))
        if choice == 1:
            print(fd.read())
        elif choice == 2:
            print(fe.read())
    if name == "Rohan":
        fe = open("rohanex.txt", "r")
        fd = open("rohandiet.txt", "r")
        choice = int(input("1. For diet\n2. For exercise\n->"))
        if choice == 1:
            print(fd.read())
        elif choice == 2:
            print(fe.read())
