# Лекция 2. Списки

#1

#Создай список fruits, содержащий названия трех любых фруктов в виде строк. Выведи этот список на экран.

fruits = ["apple", "banana", "orange"]

print(fruits)

#2

# Дан список:
# numbers = [10, 20, 30, 40, 50]
# Выведи на экран третий элемент этого списка (индексы начинаются с 0).

numbers = [10, 20, 30, 40, 50]

result = numbers[2]

print(result)

#3

# Дан список:
# animals = ["cat", "dog"]
# 1. Добавь в конец списка строку "bird".
# 2. Замени первый элемент на "hamster".
# Выведи изменённый список.

animals = ["cat", "dog"]

animals.append("bird")

animals[0] = "hamster"

print(animals)

#4

# Дан список:
# colors = ["red", "blue", "green"]
# Вставь строку "yellow" между "red" и "blue" (на позицию с индексом 1). Выведи список.

colors = ["red", "blue", "green"]

colors.insert(1, "yellow")

print(colors)

#5

# Дан список:
# languages = ["Python", "Java", "C++", "JavaScript"]
# 1. Удали "C++" из списка по значению.
# 2. Очисти список полностью.
# 3. Выведи результат после каждого шага.

languages = ["Python", "Java", "C++", "JavaScript"]

languages.remove("C++")
print(languages)

languages.clear()
print(languages)

#6

# Создайте список fruits с элементами: "яблоко", "банан", "апельсин"
# Затем выведите второй элемент списка
# Ваш код ниже

fruits = ["яблоко", "банан", "апельсин"]

print(fruits[1])

#31

# Дан список:
# numbers = [1, 2, 3]
# Добавьте число 4 в конец списка и выведите обновлённый список
# Ваш код ниже

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

#7

# Дан список:
# pets = ["кошка", "собака", "хомяк", "попугай"]
# Удалите "хомяк" из списка и выведите результат
# Ваш код ниже

pets = ["кошка", "собака", "хомяк", "попугай"]

pets.remove("хомяк")

print(pets)