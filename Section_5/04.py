sum_even = 0
last_number = int(input('Qual o valor final? '))
for n in range(0, last_number + 1, 2):
    sum_even += n

print(sum_even)
