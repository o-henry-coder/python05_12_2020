try:
    number = int(input('enter the number, which factorial should be calculated '))
    fact = 1
    for i in range(1,number + 1):
        fact *=i
        print(i, end='*')
    print(' = ', fact)
except ValueError:
    print ('the number is not integer')

