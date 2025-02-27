# this class will handle the random generation of cars
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# Car random start coordinates
Y_RAND_START = 240
X_RAND_START = 310




class CarManager():
    def __init__(self):
       self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.speed("fastest")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))

            y_cor_start = random.randint(-240, 240)
            new_car.goto(X_RAND_START, y_cor_start)
            self.all_cars.append(new_car)


    def move_cars(self, level):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT))


    def car_collision(self, player_turtle):
        for car in self.all_cars:
            if player_turtle.distance(car) < 20:
                return True
