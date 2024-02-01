# Adicionando a altura dos alunos em uma lista
students_heights = input('Digite a altura dos alunos: ').split(', ')
students_qty = len(students_heights)
sum_students_height = 0
average_students_height = 0
max_height = []
min_height = 0

# Transformando em inteiro:
for n in range(0, students_qty):
    students_heights[n] = int(students_heights[n])
    sum_students_height += students_heights[n]

max_height = max(students_heights)
min_height = min(students_heights)
average_students_height = sum_students_height / students_qty

print(average_students_height)
print(max_height)
print(min_height)
