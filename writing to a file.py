f=open("Hardik1.txt","w")       #Write mode
#if file already exist then it will replace the file. Otherwise it will make a file file automatically
f.write("Hardik bhai bohot acche hai\n")
f.write("Hardik bhai bohot acche hai\n")
f.write("Hardik bhai bohot acche hai\n")
a=f.write("Hardik bhai bohot acche hai\n")
print(a)            #prints number of characters wriiten in file
f.close()

#########################################################################
#Both read and writing simultaneously
f=open("Hardik1.txt","r+")
print(f.read())
f.write("Yes, I agree")
f.close()