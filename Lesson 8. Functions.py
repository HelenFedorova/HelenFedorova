# Лекция 8. Функции

# 1
# Напиши функцию greet(), которая выводит в консоль сообщение "Привет, мир!".
# Пример вызова:
# greet()
# Ожидаемый вывод:
# Привет, мир!

def greet():
    print("Привет, мир!")

greet()

# 2
# Напиши функцию multiply(a, b), которая принимает два числа и возвращает их произведение.
# Пример вызова:
# result = multiply(3, 4)
# print(result)  # Ожидаемый вывод: 12

def multiply(a,b):
    return a * b

result = multiply(2,5)

print(result)

# 3
# Напиши функцию welcome(name, greeting="Привет"),
# которая принимает имя и приветствие (по умолчанию "Привет"),
# а затем возвращает строку "[greeting], [name]!".
# Примеры вызова:
# print(welcome("Анна"))           # Ожидаемый вывод: "Привет, Анна!"
# print(welcome("Иван", "Здравствуй"))  # Ожидаемый вывод: "Здравствуй, Иван!"

# def welcome(name, greeting = "Привет"):
#     print(f"{greeting}, {name}, !")

def welcome(name, greeting = "Привет"):
    return f"{greeting}, {name}!"

print(welcome("Анна"))
print(welcome("Иван", "Здравствуй"))

# 4
# Напиши функцию is_even(num), которая принимает число и возвращает:
# - True, если число чётное,
# - False, если число нечётное.
# Примеры вызова:
# print(is_even(4))  # Ожидаемый вывод: True
# print(is_even(7))  # Ожидаемый вывод: False

def is_even(num):
    if num %2:
        return (False)
    else:
        return (True)

print(is_even(4))
print(is_even(7))

# 5
# Напиши декоратор `uppercase_decorator`, который преобразует
# возвращаемую строку декорируемой функции в ВЕРХНИЙ РЕГИСТР.
# Пример использования:
# @uppercase_decorator
# def say_hello():
#     return "hello"
# print(say_hello())  # Ожидаемый вывод: "HELLO"
# Твой код здесь (сначала объяви декоратор, потом проверь его на функции say_hello)

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello"

print(say_hello())
