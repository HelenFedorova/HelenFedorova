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