#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry.
# The hat decides which of the four "Houses" each first-year student goes to:
#🦁 Gryffindor
#🦅 Ravenclaw
#🦡 Hufflepuff
#🐍 Slytherin

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Welcome to the Sorting Hat Quiz!')
print('Answer the following questions to find out which Hogwarts house you belong to.')

# Question 1
print(f'Do you like Dawn or Dusk?'
    f'\n1) Dawn'
    f'\n2) Dusk')
answer1 = int(input('Enter 1 or 2: '))
if answer1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input.')
    exit()

# Question 2
print(f'When Im dead, I want people to remember me as:'
    f'\n1) The Good'
    f'\n2) The Great'
    f'\n3) The Wise'
    f'\n4) The Bold')
answer2 = int(input('Enter 1, 2, 3 or 4: '))
if answer2 == 1:
    Hufflepuff += 2
elif answer2 == 2:
    Slytherin += 2
elif answer2 == 3:
    Ravenclaw += 2
elif answer2 == 4:
    Gryffindor += 2
else:
    print('Wrong input.')
    exit()

# Question 3
print(f'Which kind of instrument most pleases you ear?'
    f'\n1) The violin'
    f'\n2) The trumpet'
    f'\n3) The piano'
    f'\n4) The drum')
answer3 = int(input('Enter 1, 2, 3 or 4: '))
if answer3 == 1:
    Slytherin += 4
elif answer3 == 2:
    Hufflepuff +=4
elif answer3 == 3:
    Ravenclaw += 4
elif answer3 == 4:
    Gryffindor += 4
else:
    print('Wrong input.')
    exit()

print('Final Scores:')
print(f'Gryffindor: {Gryffindor}'
      f'\nRavenclaw: {Ravenclaw}'
      f'\nHufflepuff: {Hufflepuff}'
      f'\nSlytherin: {Slytherin}')


if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print('You belong to Gryffindor!')
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print('You belong to Ravenclaw!')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print('You belong to Hufflepuff!')
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print('You belong to Slytherin!')
else:
    print('You have a tie between two or more houses. Please retake the quiz to get a definitive answer.')

