def varcount(*var):
    count=0
    for i in var:
        count+=1
    print("\nThe number of variables passed to the functions are: ",count)

varcount(12,32,35,64,54,32)