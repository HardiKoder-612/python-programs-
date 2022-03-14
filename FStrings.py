# F Strings
import math
#First we take an example of normal string
me="Hardik"
a1="3"
a="This is %s and %s"%(me,a1)       #in place of (%s), it will replace the string in brackets respectively
print(a)
#######################################################################################################################################################
"""
But above method is not user friendly and fast, therefore we use f strings for formatting strings
"""
b=f"this is {me} {a1} {math.cos(45)}"           # it will enter the data in place of {}, and f denotes fast
print(b)