entered_number = int(input('enter any number in range 0f 1 - 100 '))
while entered_number < 1 or entered_number > 100:
    print('the entered number is out of this range')
    entered_number = int(input('enter any number in range 0f 1 - 100 '))
print('thank you, the number is in range')