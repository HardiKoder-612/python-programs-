#Sets are made in python using the help of lists

# #Method 1 to define the list
# s=set()                                         #Empty set
# s_from_list=set([1,2,3,4,5])                #non-empty set
# print(s_from_list)
# print(type(s_from_list))

#Method 2
l=[2,3,4,5]
slist=set(l)
print(slist)

#adding elements in a set
slist.add(1)                                #it will add 1 to the set at front
print(slist)
print(len(slist))                           #print length of set
#if we again add 1 to the set, it will not be inserteed again, and thats the difference between list and set
#Set only retain unique values

#Set functions

s1=slist.union({1,5,6,7})
print(s1)
s1=slist.intersection({1,2})
print(s1)
print(s1.isdisjoint(slist))

#deleting an element
slist.remove(2)                 #removes two from the set
print(slist)
