age = int(input("Enter age "))
hour = int(input("Enter hour "))
can_buy_alcohol = age > 18 and hour < 22
print("can buy alcohol = ", can_buy_alcohol)

can_buy_sigar = age > 18 or hour < 22
print("can buy sigar = ", can_buy_alcohol)