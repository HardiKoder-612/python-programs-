#In write mode if a file already exist and we again open thatfile and write something in it, then old text of the file will be replaced by the new file text
#But in append mode, text will not be replaced, new text will the written at the end of the file
f=open("Hardik2.txt","a")
f.write("Hardik bohut accha hai\n")
f.write("Maano ya na maano")
f.close()
