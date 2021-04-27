# class RetailItem:
#     def __init__(self, description, quantity, price):
#         self.description = description
#         self.quantity = quantity
#         self.price = price
#
# class CashRegister:
#     def purchase_item(self,item_object):
#         self.item_object = item_object
#         item_list = [item_object]
#         return item_list


    # def show(self):
    #     print("the item description: ", self.description)
    #     print("the item quality: ", self.quantity)
    #     print("the item price: ", self.price)
    #     print("____________________________________________________")

class RetailItem:
    def __init__(self, desc, price, quantity):
        self.size = desc
        self.price = price
        self.q = quantity


class CashRegister:
    def __init__(self):
        self.retail_items = []

    def purchase_item(self, item):
        self.retail_items.append(item)

    def get_total(self):
        return sum([i.price * i.q for i in self.retail_items])

    def __str__(self) :
        return repr(self.retail_items)



cash_register = CashRegister()
c1 = cash_register.purchase_item(RetailItem('jeans', 100, 1))
cash_register.purchase_item(RetailItem('t-short', 10, 2))

retail_item = []
retail_item.append(c1)
print(c1)
# retail_item.append(cash_register.purchase_item(RetailItem('t-short', 10, 2)))

print(retail_item)
print(cash_register.purchase_item)
print(cash_register.get_total())
