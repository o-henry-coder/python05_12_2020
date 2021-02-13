import tkinter
import tkinter.messagebox
from ua.univer.lesson09.videoteka_main import *

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
        self.rb4 = tkinter.Radiobutton(self.top_frame, text='variant 4', variable=self.radio_var, value=4)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()


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
        # tkinter.messagebox.showinfo('choice', 'the variant is chosen' + str(self.radio_var.get()))
        # self.message = 'you have chosen:\n'

        if self.radio_var.get() == 1 :
            with sqlite3.connect('movie_database.sqlite') as conn :
                cursor = conn.cursor()
                cursor.execute('SELECT films.title, films.date, films.country from films')
                results = cursor.fetchall()
                films = []
                for entry in results :
                    films.append(Films(title=entry[0], date=entry[1], country=entry[2]))
                    # print(entry, '\n')
                tkinter.messagebox.showinfo('choice', entry.__str__())
                conn.commit()

        if self.radio_var.get() == 2 :
            tkinter.messagebox.showinfo('all films', Requests.show_all_films())
        if self.radio_var.get() == 3 :
            self.message = self.message + '3\n'
        if self.radio_var.get() == 4 :
            self.message = self.message + '3\n'

        # tkinter.messagebox.showinfo('choice', Requests.show_all_films())

my_gui = MyGUI()
