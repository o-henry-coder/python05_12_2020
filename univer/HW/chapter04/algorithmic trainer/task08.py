entered_number = float(input('enter any positive number > 0 '))
while entered_number <= 0:
    print('the entered number is out of this range')
    entered_number = float(input('enter any other positive number > 0 '))
print('thank you, the number is in range')