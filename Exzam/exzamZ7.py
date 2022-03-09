# адача 1:
# Построить три класса (базовый и 3 потомка),
# описывающих некоторых хищных животных (один из потомков),
# всеядных(второй потомок) и травоядных (третий потомок).
# Описать в базовом классе абстрактный метод для расчета количества и типа пищи,
# необходимого для пропитания животного в зоопарке.



from abc import ABC, abstractmethod
class Animal(ABC):
    def __int__(self, name, nutrition):
        self.name = name
        self.nutrition = nutrition
    def print(self):
        print("Животное :", self.name)
        print("Тип питания :", self.nutrition)

class wolf(Animal):
    def __init__(self, name, nutrition, quantity_of_food):
        super().__init__(self, name, nutrition)
        self.quantity_of_food = quantity_of_food
        self.name = name
        self.nutrition = nutrition
    def print_wolf(self):
        print("Животное :", self.name)
        print("Тип питания :", self.nutrition)
        print("Ест", str(self.quantity_of_food), "кг мясо.")
class dog(Animal):
    def __init__(self, name, nutrition, quantity_of_food):
        super().__init__(self, name, nutrition)
        self.quantity_of_food = quantity_of_food
        self.name = name
        self.nutrition = nutrition
    def print_dog(self):
        print("Животное :", self.name)
        print("Тип питания :", self.nutrition)
        print("Ест", str(self.quantity_of_food), "кг еды.")

a = wolf("волк", 'хищник', 50)
a.print_wolf()




