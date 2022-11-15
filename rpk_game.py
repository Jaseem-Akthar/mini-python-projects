import random

uwins = 0
cwins =0

options = ['rock', 'paper', 'scissors']

while True:
    uinput = input('Type Rock/Paper/Scissors or Q to Quit: ').lower()
    if uinput == 'q':
        break

    if uinput not in options:
        continue

    random_num = random.randint(0, 2)
    #rock =0, paper = 1, scissors = 2
    comp_pick = options[random_num]
    print('Computer Picked ', comp_pick + '.')

    if uinput == 'rock' and comp_pick == 'scissors':
        print('You Won!!! ')
        uwins += 1

    elif uinput == 'paper' and comp_pick == 'rock':
        print('You Won!!! ')
        uwins += 1
        
    elif uinput == 'scissors' and comp_pick == 'paper':
        print('You Won!!! ')
        uwins += 1
        
    else:
        print('You Lost!! ')
        cwins += 1
    
print('You Won', uwins, 'times')
print('The Computer Won', cwins, 'times')
print('Good Attempt!! ')
