class RetailItem:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

    def show(self):
        print("the item description: ", self.description)
        print("the item quality: ", self.quantity)
        print("the item price: ", self.price)
        print("____________________________________________________")




