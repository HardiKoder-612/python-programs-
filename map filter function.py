#******************************************MAPS********************************************
"""
"A map function executes certain instructions or functionality provided to it on every item of an iterable."
"""
items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x*3), items))
print(a)
#Output: [1, 8, 27, 64, 125]
#******************************************FILTER********************************************
"""
"A filter function in Python tests a specific user-defined condition for a function and returns an iterable 
for the elements and values that satisfy the condition or, in other words, return true."
"""
a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c)
# prints out [2, 5, 3]
#******************************************REDUCE********************************************
"""
"Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".
"""
from functools import reduce
a=reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print(a)