import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([0,-1, 1]) # Generates a random choice between 0, -1 and 1
youStr = input("Enter Your Choice: ")
youDict = {"s": 1, "w": -1, "g":0}
reverseDict = {-1: "Water", 0: "Gun", 1: "Snake"}
you = youDict[youStr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer == you):
    print("It's a draw !")

else:
    if(computer == 1 and you == -1):
        print("You Lose !")
    elif(computer == 1 and you == 0):
        print("You Win !")
    elif(computer == -1 and you == 1):
        print("You Win !")
    elif(computer == -1 and you == 0):
        print("You Lose !")
    elif(computer == 0 and you == -1):
        print("You Win !")
    elif(computer == 0 and you == 1):
        print("You Lose !")

    else:
        print("Something went wrong !")