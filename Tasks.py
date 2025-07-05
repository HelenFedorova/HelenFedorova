# 1
# Даны две переменные: a = "123" и b = 456
# Преобразуй их к нужным типам и выведи сумму a и b
from operator import truediv

a = "123"
b = 456

a_str = int(a)

print(a_str + b)

print(type(a_str))
print(type(b))

# 2
# Даны переменные: x = 10, y = 3.
# Выведи результат деления x на y,
# а затем результат целочисленного деления x на y.

x = 10
y = 3

print(x/y)

print(x//y)

# 3
# Даны переменные: p = 15, q = 20.
# Проверь, что p меньше q, и выведи результат проверки.
# Затем проверь, что p не равно q, и также выведи результат/

p = 15
q = 20

result = p < q
result2 = p != q

print(result)
print(result2)

#4
# Создай переменную, хранящую количество студентов в группе,
# используя snake_case нотацию. Затем выведи её значение.

students_group = 20

print(students_group)

#5
# Объяви три переменные:
# - name (строка) — твоё имя,
# - age (число) — твой возраст,
# - is_student (булево значение) — является ли студентом.
# Выведи их значения в одной строке через запятую.

name = "Helena"
age = 26
is_student = True

print(name, age, is_student)

#6
# Даны значения: 42, "42", 42.0, True.
# Определи тип каждого значения и выведи в формате:
# "Значение: 42, тип: <тип>".

a = 42
b = "42"
c = 42.0
d = True

print("Значение:", a, "тип:", type(a))
print("Значение:", b, "тип:", type(b))
print("Значение:", c, "тип:", type(c))
print("Значение:", d, "тип:", type(d))

#7
# Дана переменная: temperature = "22.5"
# Преобразуй её в тип float, затем в int
# Выведи оба преобразованных значения и их типы

temperature = "22.5"

temperature_float = float(temperature)
temperature_int = int(temperature_float)

print(temperature_float, type(temperature_float))
print(temperature_int, type(temperature_int))

#8
# Даны переменные: a = 10, b = 3
# Выполни и выведи результаты:
# 1) Возведение a в степень b
# 2) Остаток от деления a на b
# 3) Умножение a на b плюс 5

a = 10
b = 3

result_degree = a ** b
result_division = a % b
result_multiplication = a * b + 5

print(result_degree)
print(result_division)
print(result_multiplication)

#9
# Объяви переменные для хранения информации о книге:
# - title (название)
# - author (автор)
# - year (год издания)
# - is_available (доступность для выдачи)
# Выведи их в формате: "Книга [название], автор [автор], [год] год"
# Затем выведи статус доступности отдельно

title = "Капитал"
author = "Карл Маркс"
year = "1867"
is_available = True

print("Книга " + title + ", автор " + author + ", " + year + " год" )
print(is_available)

#10
# Даны переменные:
# x = 15
# y = 20
# z = 10

# Проверь и выведи результаты:
# 1) x < y и z < y
# 2) x > z или y < z
# 3) not (x == y)

x = 15
y = 20
z = 10

result1 = x < y and z < y
result2 = x > z or y < z
result3 = not (x == y)

print(result1)
print(result2)
print(result3)

#11
# Даны переменные:
# a = 7
# b = 3

# Выведи результаты:
# 1) Сложение a и b
# 2) Умножение a на b
# 3) Целочисленное деление a на b

a = 7
b = 3

result1 = a + b
result2 = a * b
result3 = a // b

print(result1)
print(result2)
print(result3)

#12
# Даны переменные:
# num_str = "15"
# num_float = 3.8

# Задание:
# 1. Преобразуй num_str в целое число
# 2. Преобразуй num_float в строку
# 3. Выведи типы полученных значений через print(type())

# Формат вывода:
# <class 'int'>
# <class 'str'>

num_str = "15"
num_float = 3.8

num_str_int = int(num_str)
num_float_str = str(num_float)

print(type(num_str_int))
print(type(num_float_str))

#13
# Даны переменные:
# a = 5
# b = 7

# Задание:
# 1. Проверь, является ли a меньше b
# 2. Проверь, равны ли a и b
# 3. Выведи оба результата построчно

# Ожидаемый формат вывода:
# True
# False

a = 5
b = 7

result1 = a < b
result2 = a == b

print(result1)
print(result2)

#14
# Даны переменные:
# price = "15.99"
# items = 3

# Задание:
# 1. Преобразуй price в число с плавающей точкой
# 2. Вычисли общую стоимость (цена × количество)
# 3. Выведи результат в формате: "Общая стоимость: XX.XX"

price = "15.99"
items = 3

price_float = float(price)
total_cost = price_float * items

print("Общая стоимость:", total_cost)

#15
# Даны переменные:
# number = "123"
# temperature = 36.6
# flag = False

# Задание:
# 1. Преобразуй number в целое число
# 2. Преобразуй temperature в строку
# 3. Преобразуй flag в целое число
# 4. Выведи полученные значения через print()

# Ожидаемый вывод:
# 123
# "36.6"
# 0

number = "123"
temperature = 36.6
flag = False

number_int = int(number)
temperature_str = str(temperature)
flag_int = int(flag)

print(number_int)
print(temperature_str)
print(flag_int)

#16
# Даны переменные:
# a = 8
# b = 3

# Задание:
# 1. Найди остаток от деления a на b
# 2. Возведи b в квадрат
# 3. Умножь a на 0.5
# 4. Выведи все результаты построчно в порядке выполнения

# Ожидаемый вывод:
# 2
# 9
# 4.0

a = 8
b = 3

result1 = a % b
result2 = b ** 2
result3 = a * 0.5

print(result1)
print(result2)
print(result3)