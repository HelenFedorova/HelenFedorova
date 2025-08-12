# Лекция 9. ООП часть 1

# 1
# Задача 1 (Создание класса)
# Создай класс Dog с двумя атрибутами: name (имя) и breed (порода).
# Атрибуты должны задаваться при создании объекта.
# Пример использования:
# my_dog = Dog("Барсик", "Двортерьер")
# print(my_dog.name)  # Должно вывести: Барсик

class Dog: # создание класса

    def __init__(self, name, breed): # создание атрибутов
        self.name = name # имя собаки
        self.breed = breed # порода собаки

my_dog = Dog("Барсик", "Двортерьер") # создание объекта класса
print(my_dog.name)

# 2
# Добавь в класс Dog метод bark(), который выводит "Гав!" при вызове.
# Пример использования:
# my_dog = Dog("Барсик", "Двортерьер")
# my_dog.bark()  # Должно вывести: Гав!

class Dog: # создание класса

    def __init__(self, name, breed): # создание атрибутов
        self.name = name # имя собаки
        self.breed = breed # порода собаки

    def bark(self): # функция вывода
        print(f"Гав!")

my_dog = Dog("Барсик", "Двортерьер") # создание объекта класса
my_dog.bark()

# 3
# Добавь метод introduce(), который использует self для доступа к атрибутам name и breed.
# Пример использования:
# my_dog = Dog("Барсик", "Двортерьер")
# my_dog.introduce()  # Должно вывести: "Я Барсик, моя порода — Двортерьер!"

class Dog: # создание класса

    def __init__(self, name, breed): # создание атрибутов
        self.name = name # имя собаки
        self.breed = breed # порода собаки

    def introduce(self):
        print(f"Я {self.name}, моя порода - {self.breed}!")

my_dog = Dog("Барсик", "Двортерьер") # создание объекта класса
my_dog.introduce()

# 4
# Создай класс Book с конструктором, принимающим title, author и pages (по умолчанию 100).
# Пример использования:
# my_book = Book("Война и мир", "Толстой Л.Н.", 1200)
# print(my_book.pages)  # Должно вывести: 1200
#
# short_book = Book("Сказки", "Пушкин А.С.")
# print(short_book.pages)  # Должно вывести: 100

class Book:

    def __init__(self, title, author, pages = 100):
        self.title = title
        self.author = author
        self.pages = pages

my_book = Book(title = "Война и мир", author = "Толстой Л.Н.", pages=1200)
print(my_book.pages)

short_book = Book(title = "Сказки", author = "Пушкин А.С.")
print(short_book.pages)
