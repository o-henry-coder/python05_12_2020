from ua.univer.HW.lesson05_oop.programming_tasks.task03_information import Information

def main():
    name = input('Enter the name of your pet ')
    address = input('Enter the type of your pet ')
    age = input('Enter the age of your pet ')
    phone = input('Enter the age of your pet ')
    my_info = Information(name, address, age, phone)

    print("Here your pet data:")
    print('the name is ', my_info.get_name())
    print('the type is ', my_info.get_address())
    print('the age is ', my_info.get_age())

main()