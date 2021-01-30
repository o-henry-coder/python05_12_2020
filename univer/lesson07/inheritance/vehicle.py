class CVehicle:
    def __init__(self, coord, price, velocity, year):
        self.coord = coord
        self.price = price
        self.velocity = velocity
        self.year = year
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value in range(1, 100000):
            self.__price = value
        else:
            self.__price = None
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        if value in range(1, 100000) :
            self.__velocity = value
        else :
            self.__velocity = None

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value in range(1800, 2021) :
            self.__year = value
        else :
            self.__year = None
            print('the year has improper value')

    def __str__(self):
        return f"{self.coord}, {self.price}, {self.velocity}, {self.year}"

class CPlane(CVehicle):
    def __init__(self, coord, price, velocity, year, height, passengers):
        CVehicle.__init__(self, coord, price, velocity, year)
        self.height = height
        self.passengers = passengers
    @property
    def passenges(self):
        return self.__passengers

    @passenges.setter
    def passenges(self, value):
        if value in range(0, 300) :
            self.__passengers = value
        else :
            self.__passengers = 0
            print('the quantity of passengers with improper value')

    def __str__(self) :
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passengers}"

class CShip(CVehicle):
    def __init__(self, coord, price, velocity, year, port, passengers):
        CVehicle.__init__(self, coord, price, velocity, year)
        self.port = port
        self.passengers = passengers

    @property
    def passenges(self) :
        return self.__passengers

    @passenges.setter
    def passenges(self, value) :
        if value in range(0, 300) :
            self.__passengers = value
        else :
            self.__passengers = 0
            print('the quantity of passengers with improper value')
    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        if value.isalpha():
            self.__port = value
        else :
            self.__port = None
            print('the port is incorrect ')

    def __str__(self) :
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passengers}"
class CCar(CVehicle):
    def __init__(self, coord, price, velocity, year):
        CVehicle.__init__(self, coord, price, velocity, year)


