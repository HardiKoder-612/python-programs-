n=18
print("You have given 9 chances to guess the number.")
chance=0
while(chance<9):
    print("Number of chances left: ",(9-chance))
    num = int(input("Enter your number to guess: "))
    chance=chance+1
    if(num<n):
        print("Enter a number greater than this.")
        continue
    elif(num>n):
        print("Enter a number less than this.")
        continue
    elif(num==n):
        print("Congratulations, you have correctly guessed the number.")
        break
    else:
        print("Game Over!!!")
