from ua.univer.HW.lesson05_oop.programming_tasks.task06_patient import Patient
from ua.univer.HW.lesson05_oop.programming_tasks.task06_patient import Procedure

def show_proced_description() :
    proced1 = Procedure('Medical Examination', 'today', 'Irvin', 250.00)
    proced1.show()
    proced2 = Procedure('X-Ray', 'today', 'Jameson', 500.00)
    proced2.show()
    proced3 = Procedure('Blood Test', 'today', 'Smith', 200.00)
    proced3.show()
    total_price = proced1.get_proced_price() + proced2.get_proced_price() + proced3.get_proced_price()
    print("The total price for the procedures is $", total_price)

def main():
    name = input('Please enter your name:  ')
    patronymic = input('Please enter your patronymic:  ')
    surname = input('Please enter your surname:  ')
    full_name = name + '\t'+ patronymic + '\t' + surname
    city = input('Please enter your city:  ')
    region = input('Please enter your region:  ')
    post_address = input('Please enter your post address:  ')
    full_address = city + '\t' + region + '\t' + post_address
    phone = input('Enter your phone ')
    extra_contact = input('Enter any extra contact ')
    patient1 = Patient(full_name, full_address, phone, extra_contact)
    patient1.show()
    print("Here is the list of your procedures")
    show_proced_description()

main()




