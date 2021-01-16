from ua.univer.HW.lesson05_oop.programming_tasks import task08_cashregister
from ua.univer.HW.lesson05_oop.programming_tasks.task08_cashregister import RetailItem, CashRegister

if __name__ == '__main__':
    item1 = RetailItem('Jacket', 12, 59.95)
    item2 = RetailItem('Trendy Jeans', 40, 34.95)
    item3 = RetailItem('Shirt', 20, 24.95)

    item = CashRegister(item1)

    print(item.purchase_item)