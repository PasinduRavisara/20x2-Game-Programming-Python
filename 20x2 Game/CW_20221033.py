import random
import datetime
import time

#Creating and initializing variables
plyer_name = 0
title_1 = 0
disp = 0
computer_start = 1000
user_start = 1000
playerPos = 0
computerPos = 0
move_count_p =0
move_count_c =0
bhCount_p=0
bhCount_c=0
p_win=0
c_win=0

#User inputs
player_name=input("Please enter your name:") #player's name

try:
    plyer_age=int(input("Please enter your age:"))#player's age
except ValueError:
    print("\nAge should be an value")


# Generate a filename based on the current date and time
fname = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M.txt")

# Enter game details into the file
with open(fname,"w") as file:
    file.write("Player's name:"+str(player_name))
    file.write("\nGame started:" +str(datetime.datetime.now()))
    file.write("\n\n\n")
    
#Creating functions

def rollDice(): #Generate random numbers by rolling the dice
    x = random.randrange(1, 7)
    return x


def start_usr():
    x = rollDice()
    print(f'Dice value is {x}')
    return x

#Creating the board
g_board = [' '] * 20
g_board[6] = 'O'
g_board[13] = 'O'


def crt_board(): #define a function to create a board
    print('-' * 60)
    print(' ' * 7 + "Player\'s Board" + ' ' *16 + "Computer\'s Board")
    print('-' * 60)
    for x in range (20):
        print("|        "," "+ g_board[x]+" ",end="")
        if x==playerPos:
            print("X            | ",end="")
        else:
            print("             | ", end="")
        print("   ", end="")
        print("  |       "," "+ g_board[x]+" ",end="")
        if x == computerPos:
            print(" X            |")
        else:
            print("              |")
    print("-" *60)    
    


#Beginning of the game

#Creating manu
title_1="Hi " + player_name + " welcome to 20x2 game"
disp = title_1.center(79)
print("\n",disp)

#Give instructions to the player
print('''\nInstructions:-
    -There are 20 blocks in the board
    -First person who goes to the 20th block wins the game
    -To start the game you must roll the dice until you get 6 as dice value\n''')

computer_start == 10000
user_start == 10000

while True:

    input('\n\nPress Enter to roll the dice...')
    print()
    user= start_usr()

    #check if player can start the game
    if user== 6:
        print("\nYou can start the game\n")
        user_start==0
        break
    else:
        print("\nYou can not start\nThe dice value must be 6 to start the game\nPlease try again")
        continue

#player moving
def p_move(position,user):
    newPosition= position + int(user/2)
    if newPosition==6 or newPosition ==13:
        print("\nHit a black hole !!!\nStart from the beginning :(")
        newPosition = 0
    elif newPosition >19:
        newPosition = 19
    return newPosition

#Keep playing
while True:
    input("\nPress Enter to roll the dice to continue the game...\n")
    user= start_usr()
    move_count_p +=1
    print("The player passes",int(user/2),"more blocks ahead")
    playerPos= p_move(playerPos,user)
    bhCount_p+=1
    crt_board()
    if playerPos ==19:
        print("\n\n")
        print(' ' * 17+" !!!Congratulations!!!")
        print(' ' * 17+"   You won the game")
        p_win=1
        break
    time.sleep(0.75)
    print("\nThe computer is going to roll the dice....")
    time.sleep(1.0)
    print("\nComputer rolled the dice\n")
    user= start_usr()
    move_count_c +=1
    print("The computer passes",int(user/2),"more blocks ahead")
    computerPos = p_move(computerPos, user)
    bhCount_c +=1
    crt_board()
    if computerPos == 19:
        print("\n\n")
        print(' ' * 16+ "The computer won the game!!!")
        print(' ' * 16+ "   Better luck next time")
        c_win=1
        break    

#Enter final details into the file
with open(fname,"a") as file:
    file.write("Human") #Details of the player
    file.write("\nTotal moves " + str(move_count_p))
    file.write("\nBlack hole hits " +str(bhCount_p))
    if p_win==1:
        file.write("\nWon the game")
    else:
        file.write("\nLost the game")


    file.write("\n\nComputer")
    file.write("\nTotal moves " + str(move_count_c))
    file.write("\nBlack hole hits " +str(bhCount_c))
    if c_win==1:
        file.write("\nWon the game")
    else:
        file.write("\nLost the game")




