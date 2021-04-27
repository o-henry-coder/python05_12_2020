import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text = 'press me',
                                        command = self.do_something)

        self.quit_button = tkinter.Button(self.main_window, text = 'quit',
                                          command = self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('reaction', 'thanks for pressing')


my_gui = MyGUI()
