# A program for calculating the area of different shapes based on dimensions input by the user

# Import math module to access pi for the circle area calculation

import math

# Print the menu the user can choose a shape from

print('==================')
print('Area Calculator 📐')
print('==================')
print(' ')
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
print(' ')

# Get user input for shape choise

shape = int(input('Which shape: '))

# Initialize area variable

area = 0

# Calculate area based on the chosen shape and the dimensions input

if shape == 1:
    print(' ')
    base = float(input('Base: '))
    height = float(input('Height: '))
    print(' ')
    area = (height*base)/2
elif shape == 2:
    print(' ')
    length = float(input('Length: '))
    width = float(input('Width: '))
    print(' ')
    area = length*width
elif shape == 3:
    print(' ')
    side = float(input('Side: '))
    print(' ')
    area = side**2
elif shape == 4:
    print(' ')
    radius = float(input('Radius: '))
    print(' ')
    area = math.pi*radius**2
elif shape == 5: # Quit option: the program ends without an area calculation
    print(' ')
    print('Goodbye!')
    exit()

# Print the calculated area

print('The area is', area)