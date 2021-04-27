import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,text = 'variant 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text = 'variant 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text = 'variant 3', variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()


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
        tkinter.messagebox.showinfo('choice', 'the variant is chosen' + str(self.radio_var.get()))


my_gui = MyGUI()
