# Desempenho do Aluno
student = {}

name = input("Name: ")
average = float(input("Average: "))

student['name'] = name
student['average'] = average

if student['average'] > 60:
    student['situation'] = 'AP'
else:
    student['situation'] = 'RP'

print(student)
