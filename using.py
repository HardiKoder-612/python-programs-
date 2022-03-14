#using python built in modules
import random
random_num=random.randint(0,5)          #selects a number from 0 to 5 includin both automatically
print(random_num)
rand=random.random()        #selects a number from 0 to 1
print(rand)
# to select from 0 to 100 multiply it with 100
lst=["Star Plus","DD1","Pogo","PewDiePie"]
choice=random.choice(lst)       #selects any one index from the list
print(choice)
lst2=[["Star Plus","Hello"],["Aaj Tak","News"],["Disney","Cartoon"]]
ch1=random.choice(lst2)
print(ch1)