class Car:
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self, speed):
        self.__speed = speed
        speed += 5

    def breek(self, speed):
        self.__speed = speed
        speed -= 5
    def get_speed(self):
        return self.__speed

