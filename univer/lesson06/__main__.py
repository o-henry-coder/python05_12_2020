from ua.univer.lesson06.currency import Currency
from ua.univer.lesson06.order import Order
from ua.univer.lesson06.product import Product


    # Currency.usd = 28.5
    # p1 = Product("Apple", 20, 1)
    # p2 = Product(name="Banana", price=25, weight=1)
    # print(p1.get_price())
    # print(p2.get_price())
    # print(p1)
    # print(p2)
    # Currency.usd = 29.5
    # print(p1.get_price())
    # print(p2.get_price())
    # print(p1)
    # print(p2)


    # p1.set_price(-100)

if __name__ == '__main__':
    order = Order()
    order.add(Product("Apple", 20, 3))
    order.add(Product("Tomato", 30, 2))
    order.add(Product("Grape", 25, 1))
    order.save_total_check()
    print(order.get_total_check())
    print(order.total_cost())
