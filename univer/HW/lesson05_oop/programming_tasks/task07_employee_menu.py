from ua.univer.HW.lesson05_oop.programming_tasks.task04_employee import Employee
#find/add/change/delete/exit

import json
def load_employees():
    try:
        with open('employees.json', 'r') as file :
            employees = file.read()
            employees_dict = json.loads(employees)
            print(employees_dict)
    except IOError:
        employees_dict = {}
    return employees_dict

def find_employees(employees):
    name = input("Enter employee name to find: ")
    print(employees.get(name, 'The employee was not found')

def add_employee(employees):
    name = input("Please enter employee name: ")
    id = input("Enter employee id: ")
    department = input("Enter department: ")
    vacancy = input("Enter vacancy: ")
    new_employee = Employee(name, id, department, vacancy)

    if id not in employees:
        employees[id] = new_employee
        print("New employee is added to the database")
    else:
        print("This employee has been already added to the database")

def change_employee(employees):
    name = input("Please enter employee name to change: ")
    if name in employees:
        id = input("Enter new employee id: ")
        department = input("Enter new department: ")
        vacancy = input("Enter new vacancy: ")
        new_employee = Employee(name, id, department, vacancy)
        employees[id] = new_employee
        print("New info is updated")
    else :
        print('The employee was not found')

def delete_employee(employees):
    name = input("Please enter employee name to delete: ")
    if name in employees:
        del employees[name]
        print('this employee was deleted')
    else :
        print('The employee was not found')

def save_employee(employees):
    with open('employees.json', 'w') as file :
        new_employee = json.dumps(employees)
        file.write(new_employee)

# def main():
#     employees = load_employees()
#
#     print("Press '1' to add employee")
#     print("Press '2' to find employee")
#     print("Press '3' to change employee")
#     print("Press '4' to delete employee")
#     print("Press '5' to exit")
#
#     choice = int(input("Choose the menu "))
#
#     if choice == 1:
#         add_employee(employees)
#     elif choice == 2:
#         find_employees(employees)
#     elif choice == 3:
#         change_employee(employees)
#     elif choice == 4:
#         delete_employee(employees)
#     else:
#         save_employee(employees)
# main()








