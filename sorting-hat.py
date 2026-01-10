# A program for sorting the user into a Harry Potter house based on their answers to questions

# Print the introduction and instructions for answering the questions

print('Answer each question with the number corresponding to your answer to get sorted into your house!')
print(' ')

# Print questions and get user input

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')
q1 = int(input())
while q1 != 1 and q1 != 2:
  print('Wrong input')
  q1 = int(input())

print("Q2) When I'm dead, I want people to remember me as:")
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')
q2 = int(input())
while q2 < 1 or q2 > 4:
  print('Wrong input')
  q2 = int(input())

print('Q3) Which kind of instrument most pleases your ear?')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')
q3 = int(input())
while q3 < 1 or q3 > 4:
  print('Wrong input')  
  q3 = int(input())

# Initialize house points variables

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0 

# Calculate house points based on user answers

if q1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif q1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1

if q2 == 1:
  hufflepuff = hufflepuff + 2
elif q2 == 2:
  slytherin = slytherin + 2
elif q2 == 3:
  ravenclaw = ravenclaw + 2
elif q2 == 4:
  gryffindor = gryffindor + 2

if q3 == 1:
  slytherin = slytherin + 4
elif q3 == 2:
  hufflepuff = hufflepuff + 4
elif q3 == 3:
  ravenclaw = ravenclaw + 4
elif q3 == 4:
  gryffindor = gryffindor + 4

# Initialize house variable

house = ''

# Determine the house with the highest points and assign it to the house variable

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  house = 'Gryffindor!'
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  house = 'Ravenclaw!'
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  house = 'Hufflepuff!'
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  house = 'Slytherin!'
else:
    print('The sorting hat is hesitating...Try again later')

# Print the house points and the house the user was sorted into

print(' ')
print('Gryffindor:', gryffindor, 'pts')
print('Ravenclaw:', ravenclaw, 'pts')
print('Hufflepuff:', hufflepuff, 'pts')
print('Slytherin:', slytherin, 'pts')
print('Your house is...', house)