# (list, tuple) Списки, кортежи

students = [1, 3, 4, 5, 12, 22, 13, 8, 9, 21, 18, 23, 2]
students = list(students)
print(students)

# data = list()
#
# while len(students) != 0:
#     print(students)
#     id_student = int(input('ID студента: '))
#     name = input(f'имя студента с ID № {id_student}: ')
#     rate = int(input(f'оценка по ответу для {name}: '))
#     data.append([name, rate])
#     students.remove(id_student)
#
# for i in data:
#     print(i)

# numbers = [i for i in range(4, 11)]
# students = ['qds', 'abc', 'wer', 'jh']

# students.reverse()
# print(students[::-1])
# students.sort()
# print(students)

# new = students.copy()
# new1 = students
#
# print(id(students))
# print(id(new1))
# print(id(new))
#
# print(new == students)
# print(new is students)



# students.append(50)
# students.insert(2, 20)
# # students.extend(numbers)
# students += numbers

# students[1] = 'teacher'
# students[0], students[2] = students[2], students[0]
# students[4:6] = 28, 'qwe'


# students.remove(18)
# del students[2], students[-3]
# deleted = students.pop(2)
# print(deleted)






# print(type(students))

# students_in_tuple = (255, 'qwerty', False)
# firs_second = students_in_tuple[:2]
# print(firs_second)

# students_in_tuple += (25.14,)

# numbers = tuple(i for i in range(1, 11))
# print(numbers)

# for student in students_in_tuple:
#     print(student.title())
#
# print(students)
#
# our_data_types = 'geektech', 312, 2.5, True
#
# print(our_data_types[2])
# print(type(our_data_types))
#
# courses = '123123'
# courses = tuple(courses)

# print(courses)
# for i in our_data_types:
#     print(type(i))

# ['abdulla', 5]
# ['adilet', 5]
# ['nazira', 5]
# ['ali', 4]
# ['aleksandr', 5]
# ['bekzat', 2]
# ['almaz', 2]
# ['kuttubai', 2]
# ['eren', 5]
# ['azamat', 2]
# ['amir', 4]
# ['ulan', 4]
# ['aitegin', 2]