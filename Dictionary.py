#Dictionary is a key-value pair
d1={}           #Syntax for creating a blank dictionary
print(type(d1))
d2={"Harry":"Burger","Rohan":"Fish","Hardik":"chicken","Shubham":{"B":"maggie","L":"roti","D":"chicken"}}     #(word:Meaning)
d2["Ankit"]="Junk Food"                 #add 'Ankit' to the dictionary
d2[420]="Kebabs"                        #adds 420 with meaning kebab in the dictioanry
print(d2)
print(d2["Harry"])      #search the meaning of 'Harry'
#print(d2['harry'])      #runtime error because h is small
print(d2["Shubham"])
print(d2["Shubham"]["B"])

del d2[420]     #delete 420 from dictionary
print(d2)

#FUNCTIONS OF DICTIONARY
d3=d2           #points same reference for both of the dictionaries. Therefore any change in one of the dictionary will affect the other also
del d3["Harry"]
print(d2)

d4=d2.copy()   #passes copy of one dictionary to another. Anychange in one will not affect the other
del d4["Hardik"]
print(d2)
print(d4)

d2.update({"Rashmi":"Channa Masala"})
print(d2)

print(d2.keys())        #prints all the keys of the dictionary
print(d2.items())       #prints all the pairs



