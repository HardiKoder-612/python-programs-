f = open("Hardik.txt")  # syntax for reading, open return pointer f
# As mode is not specified, therefore, this file will be openned in read-text mode
content = f.read()  # if no argument given, it will stores the whole content of the file in content variable
print(content)

f.close()
####################################################
f = open("hardik.txt", "rt")  # opens file in read-text mode
content = f.read(3)  # reads the first 3 charcters of the file
print(content)
content = f.read(3)  # read the next three characters of the file
print(content)
f.close()
#####################################################
# Special case for read function
f = open("Hardik.txt", "rt")
cont = f.read(3333)  # If in this cont, all the data of the file is stored, it will skip/ignore the next cont statement
print("1. ", cont)
cont = f.read(33)
print("2. ", cont)  # line 19,20 will be skipped
f.close()
#####################################################
f = open("Hardik.txt")
content = f.read()
# To print character by character from the file
for line in content:
    print(line)
# to print line by line from file
f.close()
f = open("Hardik.txt")
# for l1 in f:
#     print(l1)           #it will have newline character by default
for l2 in f:
    print(l2, end="")  # it will not have a new-line character by default
f.close()

# readline function
f = open("Hardik.txt")
print(f.readline())  # Reads the first line of the file
print(f.readline())  # reads the next line from the file
f.close()

#####################################################
# converting the file into a list
f = open("Hardik.txt")
print(f.readlines())  # readlines will print in the form of list
f.close()
