from ua.univer.lesson07.inheritance.vehicle_main import Vehicles


class Test_Vehicle(Vehicles):
    def __init__(self, vehicles):
        Vehicles.__init__(self, vehicles)

    def test_get_minprice(self):
        min_price_exp = 6720
        min_price_act = self.vehicles.get_minprice()
        if min_price_exp == min_price_act:
            print("correct")
        else:
            print("error")
