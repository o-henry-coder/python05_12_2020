from ua.univer.lesson07.inheritance.vehicle import *


class Vehicles:
    def __init__(self,vehicles =[]):
        self.vehicles = vehicles

    def add_vehicle(self, vehicle):
        for vehicle in self.vehicles:
            if isinstance(vehicle, CCar) or isinstance(vehicle, CShip) or isinstance(vehicle, CPlane):
                self.vehicles.append(vehicle)
        return self.vehicles

    def get_maxprice(self):
        max = self.vehicles[0][1]
        for max_price in self.vehicles :
            if max_price[1] > max :
                max = max_price[1]
        return max, max_price

    def get_minprice(self):
        min = self.vehicles[0][1]
        for min_price in self.vehicles :
            if min_price[1] < min :
                min = min_price[1]
        return min

    def get_price_less(self, less_price = 10000, after_year = 2000):
        for item in self.vehicles:
            if item[1] < less_price and item[3] > after_year:
                return item


    def get_class_objects(self):
        car_list =[]
        plane_list = []
        car_count = 0
        plane_count = 0
        for machine in self.vehicles:
            if isinstance(machine, CCar):
                car_count+=1
                car_list.append(machine)
            if isinstance(machine, CPlane):
                plane_count+=1
                plane_list.append(machine)
        print('the car objects are ', len(car_list))
        print('the plane objects are ', len(plane_list))
        return len(car_list), len(plane_list)
        # print('the plane objects are ')
        # return len(car_list)
        # return car_list

    def __repr__(self):
        return f"{self.vehicles}"

if __name__ == '__main__':
    # vehicles_list = Vehicles()
    #
    # plane1 = "12°05'20'", 6720, 235, 2007, 2100, 59
    # car1 = "14°08'70'", 7678, 80, 1995
    # ship1 = "14°08'70'", 7678, 80, 1900, 'Cuba', 520
    # plane2 = "12°05'20'", 56596, 235, 1958, 2100, 59
    # car2 = "14°08'70'", 7378, 80, 1995
    # ship2 = "14°08'70'", 7678, 80, 1900, 'Chernomorsk', 520
    #
    # vehicles = [plane1,car1, ship1, plane2, car2, ship2]
    # for each in vehicles:
    #     print(each)
    #     vehicles_list.add_vehicle(each)
    # print(vehicles_list)
    #
    # print(vehicles_list.get_minprice())
    # print(vehicles_list.get_maxprice())
    # print(vehicles_list.get_price_less())


    plane11 = CPlane("12°05'20'", 56576, 235, 1958, 2100, 59)
    car11 = CCar("14°08'70'", 7678, 80, 1995)
    ship11 = CShip("14°08'70'", 7678, 80, 1900, 'Cuba', 520)
    plane22 = CPlane("12°05'20'", 56576, 235, 1958, 2100, 59)
    car22 = CCar("14°08'70'", 67678, 90, 1995)
    ship22 = CShip("14°08'70'", 7678, 80, 1900, 'Chernomorsk', 520)
    # Test_Vehicle.test_get_minprice(vehicles.get_minprice())


    machines_list = Vehicles([])
    machines = [plane11, car11, ship11, plane22, car22, ship22]
    for machine in machines :
        print(machine)
        machines_list.add_vehicle(machine)
    print(machines_list)
    # print('the car objects are ')
    print(machines_list.get_class_objects())
    print(machines_list.get_maxprice())

