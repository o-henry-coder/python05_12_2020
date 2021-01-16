
from ua.univer.HW.lesson05_oop.programming_tasks.task07_employee_menu import load_employees, add_employee, \
    find_employees, change_employee, delete_employee, save_employee


class Employee:
    def __init__(self, name, id, department, vacancy):
        self.name = name
        self.id = id
        self.department = department
        self.vacancy = vacancy

    def show(self):
        print("the employee name: ", self.name)
        print("the employee ID number: ", self.id)
        print("the employee department: ", self.department)
        print("the employee vacancy: ", self.vacancy)
        print("____________________________________________________")

    # def set_name(self, name):
    #     self.name = name
    # def set_id(self, id):
    #     self.id = id
    # def set_department(self, department):
    #     self.department = department
    # def set_vacancy(self, vacancy):
    #     self.vacancy = vacancy
    #
    # def get_name(self):
    #     return self.name
    # def get_id(self):
    #     return self.id
    # def get_department(self):
    #     return self.department
    # def get_vacancy(self):
    #     return self.vacancy

def main():
    employees = load_employees()

    print("Press '1' to add employee")
    print("Press '2' to find employee")
    print("Press '3' to change employee")
    print("Press '4' to delete employee")
    print("Press '5' to exit")

    choice = int(input("Choose the menu "))

    if choice == 1:
        add_employee(employees)
    elif choice == 2:
        find_employees(employees)
    elif choice == 3:
        change_employee(employees)
    elif choice == 4:
        delete_employee(employees)
    else:
        save_employee(employees)
main()

