from datetime import date, datetime, time
import json
from datetime import date

from ua.univer.lesson06.currency import Currency


class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.set_price(price)
        self.set_weight(price)

    def set_price(self, value):
        if value > 0:
            self.__price = value/Currency.usd
        else:
            self.__price = None
            # str_err = "Error price, value < 0 in Product, " + str(datetime.now())
            # print(str_err)
            # dict_err = {'error': str_err,
            #             "class": Product,
            #             "time": datetime.now()}
            # strData = json.dumps(dict_err)
            # with open('err.json', 'a') as file:
            #     file.write(strData)
            # if self.__price != None:
            #     print("Error price")
            # else:
            #     self.__price = None

    def get_price(self):
        return self.__price * Currency.usd

    def get_name(self) :
        return self.__name

    def set_weight(self, value):
        if 0<value<100:
            self.__weight = value
        else:
            self.__weight = None
            print("Error weight")
    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name}, {self.__price}, {self.__weight}"

