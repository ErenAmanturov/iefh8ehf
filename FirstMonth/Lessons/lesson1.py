#Введение в Пайтон  : Встроенные функции , переменные, комментарии
#Базовые типы данных : строки , целые и дробные
#
name = 'eren'
surname = 'amanturov'
age = 17
height = 1.85


#Как нельзя
#1var
#var!


print ( type(name))
print (type(age))
print(type(height))

print('Hello World')

print(name, surname)
print(name + '' , surname)
print('{} {})'.format(name,surname) )
print(f'{name.title()} {surname}')
print(surname.capitalize(), name.title())
# capitilize - только первая буква  заглавная title -  каждое слово заглавная
print(2022)

print(3.6)
a = 4
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print( a // b)
print(a ** b)



#степень - ** не float - // при а и b



