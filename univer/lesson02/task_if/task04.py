#4. Даны имена 2х человек (тип string). Если имена равны,
# то вывести сообщение о том, что люди являются тезками.
def namesake(name1, name2):
    if name1 == name2:
        print('the names are the same')
    else:
        print('the names are different')


def task04_tezki() :
    name1 = input('enter the first name ')
    name2 = input('enter the second name ')
    namesake(name1, name2)
