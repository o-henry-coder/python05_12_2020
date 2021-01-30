class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, client_id, client_agreement = bool(1)):
        Person.__init__(self, name, address, phone)
        self.client_id = client_id
        self.client_agreement = client_agreement

    def set_client_agrrement(self):
        if self.client_agreement :
            print('Thank yor for response')
        else:
            print("you will not receive notification")
    def get_agreement(self):
        return self.client_agreement


if __name__ == '__main__':
    name = input('enter name ')
    address = input('address ')
    phone = input('phone ')
    client_id = input('id ')
    client_aggreement = input('please enter any key to aggree to mail notif or not')
    client = Customer(name, address, phone, client_id, client_aggreement)
    client.set_client_agrrement()


