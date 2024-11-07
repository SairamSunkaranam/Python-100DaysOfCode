def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 2, 3, 4, 5)

class Car:

    def __init__(self, **kw):
        self.brand = kw.get("brand")
        self.model = kw.get("model")

car = Car(brand="swift", model="2013")
print(car.brand)