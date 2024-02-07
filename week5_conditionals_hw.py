'''
#1. Program that takes a digit and returns corresponding word
list1 = ['zero', 'one', 'two', 'three','four','five','six','seven','eight','nine']

num = int(input('Enter a digit between 0 and 9:'))

print(list1[num])

dict1 = {
    0: 'zero',
    1: 'one',
    2: 'two'
}

print(dict1.get(num))

#2. Rock Paper Scissors Game
# Rock Paper Scissors ASCII Art

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random

# rand_num = random.random() # generates a random value between 0 and 1
# print(round(rand_num,2))
user_move = input('Pick a move: rock/paper/scissors: ')
rand_num = round(random.random(), 2)
comp_move = ''

if rand_num >= 0 and rand_num <1/3:
    comp_move = 'rock'
elif rand_num >= 1/3 and rand_num <2/3:
    comp_move = 'paper'
else:
    comp_move = 'scissors'

result = ''

if user_move == comp_move:
    result = 'Tie.'
elif user_move == 'rock':
    if comp_move == 'paper':
        result = 'You lose!'
    else:
        result = 'You win!'
elif user_move == 'paper':
    if comp_move == 'rock':
        result = 'You win!'
    else:
        result = 'You lose!'
elif user_move == 'scissors':
    if comp_move == 'rock':
        result = 'You lose!'
    else:
        result = 'You win!'

print(f'You picked {user_move}. Computer picked {comp_move}. {result}')

#3. Enter year as input and check whether it is a leap year or not

year = int(input('Enter a year to find if it is a leap year: '))
result = ''
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = "That is a leap year!"
        else:
            result = 'That is not a leap year!'
    else:
        result = 'That is a leap year!'
else:
    result = "That is not a leap year!"

print({result})
'''

#4. Logic flowchart ###use .lower() after input
print('Welcome to Treasure Island! Your mission to to find the treasure.')
direction = input('Would you like to go left or right: ')
result = ''
if direction == 'left':
    decision = input('You found a pond! Swim or wait: ')
    if decision == 'swim':
        print('Attacked by trout. Game over.')
    elif decision == 'wait':



elif direction == 'right':
    print('Fall into a hole. Game over.')
else:
    print('Fall into hole. Game over.')