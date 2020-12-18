velocity = int(input('what is the velocity of your vehicle '))
time = int(input('enter how many hours the vehicle was riding '))
print('time', '\t', 'distance')
print('_______________')
for time in range(1, time + 1):
    distance = velocity * time
    print(time,'\t','\t',distance)