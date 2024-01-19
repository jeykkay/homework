class Car:
    PRICE = 40

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f'Make: {self.make}\nModel: {self.model}'
