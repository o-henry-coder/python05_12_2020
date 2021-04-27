# import tkinter
#
# class MyGUI:
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.label1 = tkinter.Label(self.main_window, text = 'Hello, world')
#         self.label2 = tkinter.Label(self.main_window, text='That is my program')
#         self.label1.pack(side = 'top')
#         self.label2.pack(side = 'bottom')
#         tkinter.mainloop()
#
#
# my_gui = MyGUI()

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text = 'Hello, world')
        self.label2 = tkinter.Label(self.top_frame, text='Hello, is it me')
        self.label3 = tkinter.Label(self.top_frame, text='you re looking for')
        self.label1.pack(side = 'top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text='Hello, world')
        self.label5 = tkinter.Label(self.bottom_frame, text='Hello, is it me')
        self.label6 = tkinter.Label(self.bottom_frame, text='you re looking for')
        self.label4.pack(side='bottom')
        self.label5.pack(side='bottom')
        self.label6.pack(side='bottom')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


my_gui = MyGUI()
