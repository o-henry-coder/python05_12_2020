class RetailItem:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

class CashRegister(RetailItem):
    def purchase_item(self,item_object):
        self.item_object = item_object
        item_list = [item_object]
        return item_list


    # def show(self):
    #     print("the item description: ", self.description)
    #     print("the item quality: ", self.quantity)
    #     print("the item price: ", self.price)
    #     print("____________________________________________________")

