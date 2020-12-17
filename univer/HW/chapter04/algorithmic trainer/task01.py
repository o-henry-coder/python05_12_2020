max_product = 100
num = int(input('enter any number '))
product = num * 10
while product < max_product:
    print(product)
    num = int(input('enter any number '))
    product = num * 10
print('sorry, this number > 100')