num=int(input("Enter the number: "))
temp=num
arm=0
rem=0
while num>0:
    rem=int(num%10)
    arm+=rem**3
    num=int(num/10)
if temp==arm:
    print("It is an Armstrong number")
else:
    print("It  is not an Armstrong number")