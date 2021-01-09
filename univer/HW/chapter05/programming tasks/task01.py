# 1. конвертер километров в мили
import TODO as TODO


def miles_converter() :
    km = float(input('enter the distance in kilometers '))
    miles = km * 0.6214
    print('thank you, this distance in miles is ', miles)

# 4. auto expenses
def car_payments() :
    credit_pay = float(input('please, enter the month credit payment '))
    insurance_pay = float(input('please, enter the month insurance payment '))
    gasoline_pay = float(input('please, enter the month gasoline payment '))
    engine_oil_pay = float(input('please, enter the month engine oil payment '))
    bus_pay = float(input('please, enter the month car bus payment '))
    maintance_pay = float(input('please, enter the month maintance payment '))
    month_sum = credit_pay + insurance_pay + gasoline_pay + engine_oil_pay + bus_pay + maintance_pay
    year_sum = month_sum * 12
    print('thank you. The overall sum for month is $', format(month_sum, ',.2f'))
    print('The overall sum for year is $', format(year_sum, ',.2f'))

# 15 the average mark ad its grade
def calc_average():
    mark = 0

    for i in range(5):
        mark = int(input('enter the mark '))
        mark +=1
    print(mark)
TODO


if __name__ == '__main__':
    calc_average()