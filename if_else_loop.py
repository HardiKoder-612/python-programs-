var1=50
var2=12
var3=int(input())
if var3>var2:                       #() not necessary, as your wish it is
    print("Greater")                #space is mandatory for indentation. Otherwise, it will give compiler error
elif  var3==var2:
    print("Equal")
else:
    print("lesser")

#IN LISTS

l1=[1,2,3,4]
var4=int(input())

#1 (in)

if var4 in l1:
    print("Yes it is in the list")
else:
    print("it is not in the list")
print(var4 in l1)                       #print true if it is present otherwise false


#2(not in)

if var4 not in l1:
    print("It is not in the list")
else:
    print("It is present in the list")

