num=int(input("Enter number to be checked: "))
temp=num
rev=0
rem=0
while num>0:
    rem=int(num%10)
    rev=rev*10+rem
    num=int(num/10)

if rev==temp:
    print("Number is a palindrome.")
else:
    print("Number is not a palindrome.")