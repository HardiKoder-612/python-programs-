mystr = "Hello Hardik, you are a good boy"  # output
print(mystr)  # Hello Hardik
print(mystr[0])  # prints at index 0
print(mystr[0:5])  # prints from index 0 to 5(0 included 5 excluded)
print(mystr[0:70])  # prints till the length of the string
print(len(mystr))  # prints string length
# Advanced slicing
print(mystr[0:5:3])  # prints from index 0 to 5 with skip of 3 character
print(mystr[0::2])  # prints from index 0 to last with skip of 2 character

print(mystr[-2:-4])  # from last start counting towards left in negative

#string function
#all these funtion returns new values, they do not change the original string
print(mystr.isalnum())          #flase because  string as spaces
print(mystr.endswith("boy"))    #checks the last word of the string
print(mystr.endswith("Hardik"))

print(mystr.count("H"))         #counts he number of 'H' in the whole string

print(mystr.capitalize())       #capitalize the first letter/first index of the string

print(mystr.find("are"))        #find and prints the index of the word 'are' in fron the string

print(mystr.lower())            #converts string to lowercase

print(mystr.upper())            #converts string to uppercase

print(mystr.replace("good","sweet"))            #replace good with sweet
