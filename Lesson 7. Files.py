# Лекция 7. Файлы

# 1
# Создай файл 'greeting.txt', запиши в него фразу "Hello, World!".
# Затем прочитай содержимое этого файла и выведи его в консоль.

with open("greeting.txt", "w", encoding='utf-8') as file:
    file.write("Hello, World!")
with open("greeting.txt", "r", encoding='utf-8') as file:
    print(file.read())

# 3
# Задача 3 (Работа с файлами)
# Создай файл 'greeting.txt', запиши в него 3 любые строки (каждая с новой строки).
# Затем прочитай и выведи только вторую строку из этого файла.

with open("greeting.txt", "w", encoding='utf-8') as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

with open("greeting.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    print(lines[1].strip())  # Выводим вторую строку (индекс 1)

# 4
# Создай файл 'greeting.txt' и запиши в него одну строку: "Привет, Python!"
# Прочитай файл и выведи его содержимое в консоль
# Используй только один контекстный менеджер with

with open("greeting.txt", "w", encoding='utf-8') as file:
    file.write("Привет, Python!")

with open("greeting.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)

# 5
# Создай файл 'greeting.txt' и запиши в него своё имя
# Выведи сообщение: "Файл создан! Проверь его содержимое."
# (Читать файл не нужно)

with open("greeting.txt", "w", encoding='utf-8') as file:
    file.write("Helena")

print("Файл создан! Проверь его содержимое.")

# 6

# Создай файл 'greeting.txt' и запиши в него одну цифру: 5
# (Выводить ничего не нужно)

with open("greeting.txt", "w", encoding='utf-8') as file:
    file.write("5")

