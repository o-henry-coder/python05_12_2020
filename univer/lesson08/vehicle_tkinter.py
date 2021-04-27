from tkinter import *
from tkinter import messagebox, filedialog

from ua.univer.lesson07.inheritance.vehicle import *


def get_vehicle():
    plane1 = CPlane("12°05'20'", 56576, 235, 1958, 2100, 59)
    car1 = CCar("14°08'70'", 7678, 80, 1995)
    ship1 = CShip("14°08'70'", 7678, 80, 1900, 'Cuba', 520)
    plane2 = CPlane("12°05'20'", 56576, 235, 1958, 2100, 59)
    car2 = CCar("14°08'70'", 67678, 90, 1995)
    ship2 = CShip("14°08'70'", 7678, 80, 1900, 'Chernomorsk', 520)
    amf = Amfibia("12°05'20'", 56576, 235, 1958)
    batmobile = BatMobile("12°05'20'", 156576, 2535, 1991)
    return [plane1, car1, ship1, plane2, car2, ship2, amf, batmobile]

def view_click():
    for vehicle in get_vehicle():
        languages_listbox.insert(END,vehicle.__str__())

def open_click():
    filename = filedialog.askopenfilename()
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            languages_listbox.insert(END,f"{row['name']} - {row['age']}")

def new_click():
    new_win_human = Tk()
    new_win_human.title("new_win_human")
    new_win_human.geometry("300x250")
    name = StringVar()
    surname = StringVar()

    name_label = Label(text="Введите имя:")
    surname_label = Label(text="Введите фамилию:")

    name_label.grid(row=0, column=0, sticky="w")
    surname_label.grid(row=1, column=0, sticky="w")

    name_entry = Entry(textvariable=name)
    surname_entry = Entry(textvariable=surname)
    name = name_entry.get()
    st = Student(name, 20)
    languages_listbox.insert(END,st.__str__())
    name_entry.grid(row=0,column=1, padx=5, pady=5)
    surname_entry.grid(row=1,column=1, padx=5, pady=5)

    new_win_human.mainloop()

def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")

root = Tk()
root.title("GUI на Python")
root.geometry("600x450")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New", command = new_click)
file_menu.add_command(label="Save")
file_menu.add_command(label="View", command = view_click)
file_menu.add_command(label="Open", command = open_click)
file_menu.add_separator()
file_menu.add_command(label="Exit")


main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu = file_menu, command = edit_click)
# main_menu.add_cascade(label="View", command = view_click)

root.config(menu=main_menu)
languages_listbox = Listbox()



languages_listbox.pack()
root.mainloop()