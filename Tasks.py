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