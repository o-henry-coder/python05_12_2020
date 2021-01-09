#2.ввести 10 целых значений с консоли и разместить в
#2 масива четные (if x%2 == 0) и нечетные (if x%2 == 1)
#3.подсчитать сколько четные и нечетные
#4 среднее арифметическое
even = []
odd = []
for n in range(10):
    n = int(input('enter any number '))
    if n % 2 == 0:
        print('that is an even number')
        even.append(n)
    else:
        print('that is an odd number')
        odd.append(n)
print('the even numbers are = ', even)
print(len(even), 'even numbers')
print(min(even), 'the min of even numbers')
print(max(even), 'the max of even numbers')

print('the odd numbers are = ', odd)
print(len(odd), 'odd numbers')
print(min(odd), 'the min of odd numbers')
print(max(even), 'the max of even numbers')






