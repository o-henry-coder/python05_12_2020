entered_number = float(input('enter any positive number > 0 '))
total = 0
entered_number = 0
while entered_number >= 0:
    entered_number = float(input('enter any other positive number > 0 '))
    total += entered_number

print('the entered number is negative')
print('the sum of positive numbers is ', total)