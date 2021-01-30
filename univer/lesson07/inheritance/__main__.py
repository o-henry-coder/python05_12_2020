from ua.univer.lesson07.inheritance.people import *

if __name__ == '__main__':
    st1 = Student('Tom', 20, 1)
    doc1 = Doctor('Haus', 50, 666666)
    fight1 = Fighter("Brusli", 30, 99, 50)
    fight2 = Fighter("Konan", 30, 50, 40)

    print(st1)
    print(doc1)
    print(fight1)
    print(fight2)
    fd = FighterDoc("F1", 1, 2, 3)

    humans = [st1, doc1, fight1, fight2, fd]
    old_human = humans[0]
    for human in humans:
        if human.age > old_human.age:
            old_human = human
    print(old_human)

    fighters = []
    for human in humans:
        if isinstance(human,Fighter):
            fighters.append(human)
    print(fighters)

    for fight in fighters:
        print(fight)