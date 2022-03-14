import time
initial =time.time()        #time() calculate the number of ticks where one tick denote one second
print(initial)
i=0
while i<40:
    print("Hardik")
    i+=1
print("Time taken for while loop to run is: ",time.time()-initial)
initial2=time.time()
for i in range(40):
    print("Hardik")
print("Time taken for for loop to run is: ",time.time()-initial2)

"""To Print Local Time"""
print(time.asctime(time.localtime(time.time())))

"""TO sleep the program"""
for i in range(20):
    print("hardik")
    time.sleep(2)                   #prints Hardik after time interval of two seconds
