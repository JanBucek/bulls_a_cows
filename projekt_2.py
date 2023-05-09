#   projekt_2.py:   Druhý projekt do Engeto Online Python Akademie

#   autor:          Jan Buček
#   email:          honzabuci@seznam.cz
#   discord:        Honza#1407

import time
import random

# Program pozdraví užitele a vypíše úvodní text
print('Hi there!')

# Program dále vytvoří tajné číslo
kombinace = random.sample(range(1, 10), 4)
cara = '-----------------------------------------------'

# Program chvíli počká, než pokračuje
time.sleep(2)

print(cara + '\n' + "I've generated a random 4 digit number for you." + '\n' +
      "Let's play a bulls and cows game." + '\n' + cara)

hodnota = True
bulls = int()
cows = int()
pokus = int()

while hodnota == True:
    cislo = input('Enter a number: ')
    cisla = [int(c) for c in cislo]

    for i, c in enumerate(cisla):
        if c == kombinace[i]:
            bulls += 1
        elif c in kombinace:
            cows += 1
    if bulls == 4:
        pokus += 1
        print(f"Correct, you've guessed the right number in {str(pokus)} guesses!")  
        hodnota = False
        break
    else:
        print(f'{bulls} bulls and {cows} cows')
        bulls = 0
        cows = 0
        pokus += 1
# Program vypíše počet bull/bulls (pokud uživatel uhodne jak číslo, tak jeho umístění),
# příp. cows/cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění).
