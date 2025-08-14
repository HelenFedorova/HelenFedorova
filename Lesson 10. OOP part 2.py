# Лекция 9. ООП часть 3

# 1
# Создай класс Animal с методом speak(), который выводит "Звук животного".
# Затем создай дочерний класс Dog, который наследует Animal и переопределяет метод speak(),
# чтобы он выводил "Гав!".
# Проверь работу, создав экземпляр Dog и вызвав его метод speak().

class Animal:

    def speak(self):
        print("Звук животного")

...
class Dog(Animal):

    def speak(self):
        print("Гав!")

dog = Dog()
dog.speak()

# 2
# Создай класс Vehicle с методом move(), выводящим "Транспорт двигается".
# Создай дочерний класс Boat, переопределяющий move() с выводом "Лодка плывет".
# Создай экземпляр Boat и вызови его метод move().

class Vehicle:

    def move(self):
        print("Транспорт двигается")

...

class Boat(Vehicle):

    def move(self):
        print("Лодка плывет")

boat = Boat()
boat.move()

# 3
# Создай класс Fruit с методом taste(), который выводит "Фрукт вкусный".
# Создай дочерний класс Apple, который наследует Fruit и переопределяет taste(),
# чтобы выводить "Яблоко сладкое".
# Создай экземпляр Apple и вызови его метод taste().

class Fruit:

    def taste(self):
        print("Фрукт вкусный")

...

class Apple(Fruit):

    def taste(self):
        print("Яблоко сладкое")

apple = Apple()
apple.taste()
