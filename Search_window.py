from tkinter import *

class SearchWindow:
    def __init__(self, master):
        self.__master = master
        print(master)
        self.__window = Toplevel(self.__master)
        self.__frame = Frame(self.__window)
        self.__frame.pack(padx=500, pady=500)

        self.make_form()
    def make_form(self):
        search_label = Label(self.__frame, text="Enter the submitted Name:")
        search_label.pack



        

