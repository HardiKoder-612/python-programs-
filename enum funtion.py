#Enum function gives indes as well as value of a list
l1=["Hardik","Ram","Sham","Mohan","Sohan"]

for index,item in enumerate(l1):
    if index%2==0:
        print(f"{item} you should buy ")
