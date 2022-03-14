str=input("Enter the word: ")
if len(str)>=3:
    temp=str[:-4:-1]
    if temp=="gni":
        print(str+"ly")
    else:
        print(str+"ing")