class Vehicle:
    def __init__(self, year, speed, brend):
        self.year= year
        self.speed = speed
        self.brend = brend
    def show_info(self):
        pass

class Bike(Vehicle):
    def __init__(self, year, speed, brend, madel, full_tyupe):
        super().__init__(year, speed, brend)
        self.madel = madel
        self.full = full_tyupe
    
    def show_info(self):
        return f"""yili {self.year},
tezligi {self.speed},
brendi {self.brend},
madeli {self.madel},
yoqilg'i turi {self.full}"""

class Car(Vehicle):
    def __init__(self, year, speed, brend, price, color):
        super().__init__(year, speed, brend)
        self.color = color
        self.price = price
    def show_info(self):
        return f"""yili {self.year},
tezligi {self.speed},
brendi {self.brend},
narhi {self.price},
rangi {self.color}"""
    
bike = Bike('2022', 300, 'yamaha', 'yamahaR3', 'benzin')
car = Car('2024', 220, 'chewralet', 15000, 'qora')

print(car.show_info())
print('\n')
print(bike.show_info())