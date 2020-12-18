print('The table of Celsius and Farenheit degrees')
print('C', '\t', 'F')
print('_________')
for celsius in range(0,21):
    farenheit = (9 / 5) * celsius + 32
    print(celsius, '\t', format(farenheit,'.1f'))