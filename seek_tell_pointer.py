f=open("hardik.txt")
print(f.readline())         #now this will update the pointer f

#To check the position of the pointer f, we use tell() function
print(f.tell())

print(f.readline())         #now this will update the pointer f
print(f.tell())

#To relocate the f pointer to our own desired location we se seek() function

f.seek(0)           #It will take the pointer to the 0th location i.e. start of the file
print(f.readline())

f.seek(10)
print(f.readline())
f.close()