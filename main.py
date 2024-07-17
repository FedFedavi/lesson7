# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы
# `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def animal_eat(self):
        print(f"{self.name} ест, не беспокойте его ")


class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} мычит му-му-му")


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} поет чирик-чирик")


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} шипит шшш-ш-ш")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} работает на позиции {self.position}")

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит животное {animal.name}")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит животное {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк")

    def feed_all_animals(self):
        for animal in self.animals:
            animal.animal_eat()

# Пример использования
bird = Bird("Соня", 2)
mammal = Mammal("Зорька", 8)
reptile = Reptile("Хамстел", 4)

employee1 = Employee("Иван", "Уборщик")
employee2 = Employee("Мария", "Ветеринар")

zoo_keeper = ZooKeeper("Джон")
veterinarian = Veterinarian("Мэри")


zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_employee(employee1)
zoo.add_employee(employee2)

zoo.add_employee(zoo_keeper)
zoo.add_employee(veterinarian)

zoo.feed_all_animals()

zoo_keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)


# Вывод всех сотрудников и животных
print("\nСотрудники зоопарка:")
for employee in zoo.employees:
    employee.work()

print("\nЗвуки животных в зоопарке:")
for animal in zoo.animals:
    animal.make_sound()

animal_list = [bird, mammal, reptile]

def animal_sound(animal):
    for i in animal_list:
        i.make_sound()

