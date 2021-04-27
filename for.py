# k = "*"
# l = "&"
# for i in range(10):
#     for j in range(5):
#             print(j, end='  ')
#     print(i)
def task_7() :
    sum = 0
    n = int(input('enter A '))
    k = int(input('enter B '))
    for line in range(n, k + 1, 1) :
        sum += line
        print(line, sum)


## For7. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.
task_7()


#enum? нужна сумма чисел
def task_39() :
    global a, b, i, j
    a = int(input('enter A '))
    b = int(input('enter B '))
    for i in range(a, b + 1, 1) :
        for j in range(i) :
            print(i, end=' ')
        print()


#for39
##Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до B включительно;
# при этом каждое число должно выводиться столько раз, каково его значение (например, число 3 выводится 3 раза).

task_39()

def task_40() :
    global a, b, i, j
    a = int(input('enter first number '))
    b = int(input('enter second number '))
    index = 0
    for i in range(a, b + 1) :
        index += 1
        for j in range(index) :
            print(i, end=' ')
        print()


#for 40
##Даны целые числа A и B (A < B). Вывести все целые числа от A до B включительно;
# при этом число A должно выводиться 1 раз, число A + 1 должно выводиться 2 раза и т. д.
task_40()
