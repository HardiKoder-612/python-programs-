import random

i = 1
uwin = 0
cwin = 0
draw = 0
print("Welcome to SNAKE WATER GUN game\n"
      "Instruction of the game are following->\n"
      "(a) This game will be played between usr and computer\n"
      "(b) Player has to enter one of the number from 1,2,3 where->\n"
      "\t1 denote snake\n\t2 denote water\n\t3 denote gun\n"
      "(c) Game will have 10 rounds and after 10th round the one with most wins will be declared as winner")
while i <= 10:
    user = int(input("Enter your choice (1/2/3): "))
    comp = int(random.randint(1, 3))
    if user == 1 and comp == 1:
        draw += 1
        print("Round ", i, " completed.")
    elif user == 1 and comp == 2:
        uwin += 1
        print("Round ", i, " completed.")
    elif user == 1 and comp == 3:
        cwin = cwin + 1
        print("Round ", i, " completed.")
    elif user == 2 and comp == 2:
        draw += 1
        print("Round ", i, " completed.")
    elif user == 2 and comp == 1:
        cwin += 1
        print("Round ", i, " completed.")
    elif user == 2 and comp == 3:
        uwin += 1
        print("Round ", i, " completed.")
    elif user == 3 and comp == 1:
        uwin += 1
        print("Round ", i, " completed.")
    elif user == 3 and comp == 2:
        cwin += 1
        print("Round ", i, " completed.")
    elif user == 3 and comp == 3:
        draw += 1
        print("Round ", i, " completed.")
    i += 1
# Outcome / Result
print("The result of the match is->\n")
if uwin > cwin:
    print("You have won the game with ", uwin, " wins, ", cwin, " losses and", draw, " draws")
elif uwin < cwin:
    print("The computer has won the game with ", cwin, " wins, ", cwin, " losses and", draw, " draws")
elif uwin == cwin:
    print("The game is draw with having ", uwin, " wins for both of the players")
print("Thank You for playing.........")
