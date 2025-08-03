# Лекция 5. Словари

# 1
# car = {"brand": "Toyota", "model": "Camry", "year": 2020}
# Выведи значение, связанное с ключом "model"

car = {"brand": "Toyota", "model": "Camry", "year": 2020}

print(car["model"])

# 2
# fruit = {"name": "apple", "color": "red"}
# 1. Добавь новый ключ "price" со значением 1.2
# 2. Измени значение ключа "color" на "green"
# Выведи получившийся словарь

fruit = {"name": "apple", "color": "red"}

fruit["price"] = 1.2
fruit ["color"] = "green"

print(fruit)

# 3
# book = {"title": "Python Basics", "author": "John Doe", "year": 2021}
# Удали ключ "year" из словаря
# Выведи получившийся словарь

book = {"title": "Python Basics", "author": "John Doe", "year": 2021}

year = book.pop("year")

print(year)
print(book)

# 4
# device = {"type": "phone", "brand": "Samsung", "price": 500}
# 1. Проверь, есть ли в словаре ключ "brand" (выведи True/False)
# 2. Проверь, есть ли в словаре значение "phone" (выведи True/False)
# 3. Выведи оба результата

device = {"type": "phone", "brand": "Samsung", "price": 500}

print("brand" in device) # Автоматически выведет True/False
print("phone" in device.values()) # Автоматически выведет True/False

# 5
# animal = {"type": "dog", "name": "Rex", "age": 3}
# 1. Выведи список всех ключей словаря
# 2. Выведи список всех значений
# 3. Выведи список всех пар (ключ, значение)

animal = {"type": "dog", "name": "Rex", "age": 3}

print(list(animal.keys()))
print(list(animal.values()))
print(list(animal.items()))

# 6
# Создай словарь student с ключами и значениями:
# name → "Alex"
# age → 20
# grade → "B"
# После создания выведи весь словарь

student = {"name": "Alex", "age": 20, "grade": "B"}

print(student)

# 7
# colors = {"red": "красный", "blue": "синий"}
# Добавь в словарь ключ "green" со значением "зелёный"
# Выведи обновлённый словарь

colors = {"red": "красный", "blue": "синий"}

colors["green"] = "зелёный"

print(colors)

# 8
# fruit = {"name": "apple", "color": "red", "price": 0.99}
# Удали ключ "price" с помощью метода .pop()
# Выведи удалённое значение и итоговый словарь

fruit = {"name": "apple", "color": "red", "price": 0.99}

fruit_del = fruit.pop("price")

print(fruit_del)
print(fruit)

# 9
# book = {"title": "Гарри Поттер", "author": "Дж. Роулинг"}
# Проверь, есть ли в словаре ключ "year" (выведи True или False)
# Если ключа нет, добавь его со значением 2001
# Выведи итоговый словарь

book = {"title": "Гарри Поттер", "author": "Дж. Роулинг"}

print("year" in book)

book["year"] = 2001

print(book)

# 10
# product = {"name": "Laptop", "price": 1500, "in_stock": True}
# 1. Обнови цену на 1300
# 2. Измени статус "in_stock" на False
# 3. Выведи итоговый словарь

product = {"name": "Laptop", "price": 1500, "in_stock": True}

product["price"] = 1300
product["in_stock"] = False

print(product)

# 11
# user = {"name": "Alice", "age": 25}
# 1. Получи значение по ключу "age" через метод .get()
# 2. Попробуй получить несуществующий ключ "city" (выведи "Ключ не найден", если его нет)
# 3. Выведи оба результата

user = {"name": "Alice", "age": 25}

print(user.get("age"))

if "city" in user:
    print("Ключ найден")
else:
    print("Ключ не найден")

# 12
# school = {
#    "class_1": {"students": 20, "teacher": "Ms. Smith"},
#    "class_2": {"students": 25, "teacher": "Mr. Brown"}
# }
# 1. Получи количество студентов в "class_1"
# 2. Добавь новый класс "class_3" с данными: students=18, teacher="Mrs. Davis"
# 3. Выведи обновлённый словарь school

school = {
    "class_1": {"students": 20, "teacher": "Ms. Smith"},
    "class_2": {"students": 25, "teacher": "Mr. Brown"}
}

print(school["class_1"]["students"])

school["class_3"] = {"students": 18, "teacher": "Mrs. Davis"}

print(school)
