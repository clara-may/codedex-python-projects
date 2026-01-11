# A program for playing rock-paper-scissors against the computer

# Initialize player and computer choices variables

player = ''
computer = ''

# Print the game menu

print('==================')
print('Rock Paper Scissors')
print('==================')
print(' ')
print('1) ✊')
print('2) ✋')
print('3) ✌️')

# Get user input for player choice

player = int(input('Pick a number: '))
while player != 1 and player != 2 and player != 3:
    player = int(input('Pick a number: '))

# Generate computer choice randomly

import random
computer = random.randint(1, 3)

# Print the choices

print(' ')
print('You chose:', player)
print('The computer chose: ', computer)

# Determine and print the winner based on the choices

if player == 1 and computer == 3:
    print('The player won!')
elif player == 2 and computer == 1:
    print('The player won!')
elif player == 3 and computer == 2:
    print('The player won!')

if computer == 1 and player == 3:
    print('The computer won!')  
elif computer == 2 and player == 1:
    print('The computer won!')
elif computer == 3 and player == 2:
    print('The computer won!')

if player == computer:
    print("It's a tie!")