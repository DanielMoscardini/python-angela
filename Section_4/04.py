import random

names_string = 'Bilbo, Frodo, Sam, Pippin, Merry'
names = names_string.split(', ')
name_index = random.randint(0, len(names) - 1)
chosen_name = names[name_index]
print(f'{chosen_name} is the one paying today!')
