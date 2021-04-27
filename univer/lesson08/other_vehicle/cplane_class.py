from ua.univer.lesson08.other_vehicle.interfaces_class import IFlyAble
from ua.univer.lesson08.other_vehicle.vehicle_class import CVehicle


class CPlane(CVehicle, IFlyAble):


    def fly(self):
        return self.speed

    def __init__(self, price, speed, year,passangers, height):
        CVehicle.__init__(self, price, speed, year)
        self.height = height
        self.passangers = passangers

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 0 < value < 11000:
            self.__height = value
        else:
            self.__height = None
    def set_engine(self):
        pass

    def show(self):
        pass

    def __str__(self):
        return f"Plane. {CVehicle.__str__(self)}, Max. height: {self.height}, Passengers: {self.passangers}"
    def __repr__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"