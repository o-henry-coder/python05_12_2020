from ua.univer.HW.lesson05_oop.programming_tasks.task01_pet import Pet

def main():
    name = input('Enter the name of your pet ')
    animal_type = input('Enter the type of your pet ')
    age = input('Enter the age of your pet ')
    new_pet = Pet(name, animal_type, age)

    print("Here your pet data:")
    print('the name is ', new_pet.get_name())
    print('the type is ', new_pet.get_animal_type())
    print('the age is ', new_pet.get_age())

main()


