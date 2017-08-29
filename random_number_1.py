import random
from math import floor

def randomizer(num2):
    num1 = floor((random.random() * num2)) + 1
    return num1

try:
    num2 = int(input('Enter a number between 1 to 10. \n Number : '))
except ValueError:
    print('Restarting...Invalid input.')
    raise SystemExit

print(randomizer(num2))
