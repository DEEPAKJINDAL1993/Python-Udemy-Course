# Usage of multiple arguments and optional keyword arguments

def add(*args):
    return sum(args)

print(add(1,2,3,4))


def calculate(n,**kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(2,add=3,multiply=5))


class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')
        self.mileage = kwargs.get('mileage')
        self.color = kwargs.get('color')


car = Car(make="Nissan",model='GT-R',year=2024,color='red')
print(car.make)
print(car.model)
print(car.year)
print(car.mileage)
print(car.color)
