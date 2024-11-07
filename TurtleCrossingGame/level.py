from car import Car
import random

class Level:

    def __init__(self):
        self.level = 1
        self.cars = []
        self.random_positions = []
        self.x_cor = (-320, 320)
        self.y_cor = (-250, 250)
        self.generate_random_cars(self.x_cor, self.y_cor, 10)

    def generate_random_cars(self, x_cor, y_cor, no_of_cars):
        for _ in range(no_of_cars):
            random_xcor = random.randint(x_cor[0], x_cor[1])
            random_ycor = random.randint(y_cor[0], y_cor[1])
            cors = (random_xcor, random_ycor)
            self.random_positions.append(cors)
            new_car = Car()
            new_car.goto(random_xcor, random_ycor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move_car()

