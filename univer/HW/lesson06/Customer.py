class Customer:
    def __init__(self, id, surn, name, patr, address, phone, cred_card, bank_id, customer_list = []):
        self.id = id
        self.surn = surn
        self.name = name
        self.patr = patr
        self.address = address
        self.phone = phone
        self.cred_card = cred_card
        self.bank_id = bank_id
        self.customer_list = customer_list

    def add_customer(self, customers):
        self.customer_list.append(customers)

    def alph_list_cust(self):
        alph_list = []
        for cust in self.customer_list:
            alph_list.append(cust[1:4])
            alph_list.sort()
        return alph_list

    def cust_with_credit_card(self):
        credit_list = []
        for card in self.customer_list:
            if card[6] in range(1100000000, 2000000000):
                credit_list.append(card[1:4])
        return credit_list

    def save_customers(self):
        with open("customers.txt", "w") as file_write:
            file_write.write(str(self.customer_list))

    def __str__(self) :
            return f"{self.id}, {self.surn}, {self.name},{self.patr}, {self.address}, {self.phone}, {self.cred_card},\
    {self.bank_id}, {self.customer_list}"


customer_list = Customer(65, 'Kulikova', 'Maria', 'Petrovna', 'Lviv', 868778758, 1000000000, 7897878)
cust1 = 65, 'Kulikova', 'Maria', 'Petrovna', 'Kharkiv', 868778758, 1000000000, 7897878
cust2 = 98, 'Petrova', 'Victoria', 'Nickolaevna', 'Kyiv', 868778758, 1100000000, 7897878
cust3 = 45, 'Sidorov', 'Michail', 'Vasilievich', 'Lviv', 868778758, 1130000000, 7897878
cust4 = 35, 'Gribova', 'Natalia', 'Valerievna', 'Vinnitsa', 868778758, 1230000000, 7897878
cust5 = 90, 'Ovchinnikov', 'Taras', 'Petrovich', 'Kharkiv', 868778758, 1340000000, 7897878
cust6 = 34, 'Avdeenko', 'Maxim', 'Victorovich', 'Lviv', 868778758, 1540000000, 7897878
cust7 = 67, 'Herzhan', 'Tetyana', 'Nickolaevna', 'Lviv', 868778758, 1780000000, 7897878

customers = [cust1, cust2, cust3, cust4, cust5, cust6, cust7]
for customer in customers:
    customer_list.add_customer(customer)
    print(customer)
print('The alphabetic list of customers')
print(customer_list.alph_list_cust())
print('the customers which credit cards in interval betrween 1100000000 and 2000000000')
print(customer_list.cust_with_credit_card())
customer_list.save_customers()