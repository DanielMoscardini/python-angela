import random

letters_qty = int(input('Quantas letras deseja na sua senha? \n'))
numbers_qty = int(input('Quantos numeros deseja na sua senha? \n'))
symbols_qty = int(input('Quantos simbolos deseja na sua senha? \n'))

aux_char = 'abcdefghijqklmnopqrstuvxyzABCDEFGHIJQKLMNOPQRSTUVWXYZ'
random_letters = random.sample(aux_char, letters_qty)
print(random_letters)

random_numbers = []
for i in range(1, letters_qty + 1):
    random_numbers.append(random.randint(1, 10))
print(random_numbers)

aux_symbols = '!@#$%^&*()_+=-~'
random_symbols = random.sample(aux_symbols, symbols_qty)
print(random_symbols)

aux = []

for i in random_letters:
    aux.append(i)

for i in random_symbols:
    aux.append(i)

for i in random_numbers:
    aux.append(i)

random_pwd = random.sample(aux, len(aux))
print(random_pwd)