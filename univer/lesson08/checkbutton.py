import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame,text = 'variant 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,text = 'variant 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,text = 'variant 3', variable=self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()


        self.ok_button = tkinter.Button(self.bottom_frame, text = 'ok',
                                        command = self.show_choice)

        self.quit_button = tkinter.Button(self.bottom_frame, text = 'quit',
                                          command = self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        self.message = 'you have chosen:\n'

        if self.cb_var1.get() == 1:
                self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
                self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
                self.message = self.message + '3\n'

        tkinter.messagebox.showinfo('choice', self.message)


my_gui = MyGUI()
