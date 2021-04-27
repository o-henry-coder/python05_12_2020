
from tkinter import *
from tkinter import messagebox, filedialog


def open_click():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    messagebox.showinfo('GUI on Python',filename)

def edit_click():

    print(root.filename)
    messagebox.showinfo('GUI on Python', 'the EDIT option is clicked')

root = Tk()
root.title("GUI on Python")
root.geometry('300x250')

main_menu = Menu()
file_menu = Menu()

file_menu.add_command(label = "New", command = open_click)
file_menu.add_command(label = "Save")
file_menu.add_command(label = "Open")
file_menu.add_separator()
file_menu.add_command(label = "Exit")

main_menu.add_cascade(label = "File", menu = file_menu)
main_menu.add_cascade(label = "Edit", menu = file_menu, command = edit_click)
main_menu.add_cascade(label = "View")

root.config(menu = main_menu)

root.mainloop()