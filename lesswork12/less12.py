class Moving:
    def move(self):
        raise NotImplemented


class Animal(Moving):
    def voice(self):
        raise NotImplemented


class Transport(Moving):
    def launch(self):
        raise NotImplemented


class Duck(Animal):
    def voice(self):
        return 'quack'

    def move(self):
        return 'swim'


class Tiger(Animal):
    def voice(self):
        return 'roar'

    def move(self):
        return 'runs'


class Car(Transport):
    def __init__(self):
        self.status = 'not_started'

    def move(self):
        if self.status == 'started':
            return 'drive'
        return 'car is not started'

    def launch(self):
        self.status = 'not_started'
        return 'launch'


duck = Duck()
tiger = Tiger()
car = Car()

print(duck.move(), duck.voice())
print(tiger.move(), tiger.voice())
print(car.launch(), car.move())
