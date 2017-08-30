import random

def random_item(x):
    random_index = random.randint(0, len(x) -1)
    random_item = x[random_index]
    return random_item

x = 'hello everyone'

print(random_item(x))
