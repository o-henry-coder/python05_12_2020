from tkinter import *
text = StringVar()
def click_btn():
    text.set("hello")
if __name__ == '__main__':
    win = Tk()
    win.title("first win")
    win.geometry("300x400")
    btn = Button(textvariable = text, command = click_btn())
    btn.pack()
    win.mainloop()