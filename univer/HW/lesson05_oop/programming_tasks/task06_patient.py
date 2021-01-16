class Patient:
    def __init__(self, full_name, full_address, phone, extra_contact):
        self.__full_name = full_name
        self.__full_address = full_address
        self.__phone = phone
        self.__extra_contact = extra_contact

    def set_full_name(self, full_name):
        self.__full_name = full_name
    def set_full_address(self, full_address):
        self.__full_address = full_address
    def set_phone(self, phone):
        self.__phone = phone
    def set_extra_contact(self, extra_contact):
        self.__extra_contact = extra_contact

    def get_full_name(self):
        return self.__full_name
    def get_full_address(self):
        return self.__full_address
    def get_phone(self):
        return self.__phone
    def get_extra_contact(self):
        return self.__extra_contact

    def show(self):
        print("Full name: ", self.__full_name)
        print("Full address: ", self.__full_address)
        print("Phone: ", self.__phone)
        print("Extra contact: ", self.__extra_contact)

class Procedure:
    def __init__(self, proced_type, date, doctor, proced_price):
        self.__proced_type = proced_type
        self.__date = date
        self.__doctor = doctor
        self.__proced_price = proced_price

    def set_proced_type(self, proced_type):
        self.__proced_type = proced_type
    def set_date(self, date):
        self.__date = date
    def set_doctor(self, doctor):
        self.__doctor = doctor
    def set_proced_price(self, proced_price):
        self.__proced_price = proced_price

    def get_proced_type(self):
        return self.__proced_type
    def get_date(self):
        return self.__date
    def get_doctor(self):
        return self.__doctor
    def get_proced_price(self):
        return self.__proced_price

    def show(self):
        print("the procedure type: ", self.__proced_type)
        print("the date of the procedure: ", self.__date)
        print("the doctor: ", self.__doctor)
        print("the price of the procedure: ", self.__proced_price)
        print("____________________________________________________")