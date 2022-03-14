name=["Hardik","Rohan","Sohan","Ram"]       #string list
print(name)
print(name[1])          #access using index
name1=["Hardik","Rohan","Sohan","Ram",56]       #mixed list
print(name)

number=[2,1,3,82,17,43,33]
number.sort()            #sorting the list      #changes original list also
print(number)
number.reverse()        #changes original list also
print(number)
print(number[1:4])
print(number[::2])
print(number[::-1])             #take always -1 only in negative using slicing
number.append(71)           #adds 71 at the end of the list
print(number)
number.insert(1,66)         # adds 66 at index 1 of the list
number.pop()                #removes last element
number.remove(33)           #removes 33 from the list
