list1=["Harry","Hardik","Ram","Ritesh"]
print(list1)        #prints whole list with brackets and all...
print("#######################")
#For loop
for i in list1:     #i start from 1
    print(i)        #it prints all the elements only
print("#######################")
# in tupples
t1=("Harry","Hardik","Ram","Ritesh")
for i in t1:
    print(i)

print("#######################")
#nested list
list2=[["Harry",1],["Hardik",3],["Ram",2],["Rajesh",10]]
for item,lolly in list2:    #item is for name and lolly is for number along with it
    print(item,"and ",lolly)
print("#######################")

#dictionary
d1=dict(list2)              #type-casting list to dictionary
for i,j in d1.items():      # .items is required to club both name and number
    print(i," and ",j)
 