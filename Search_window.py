from tkinter import *

class SearchWindow:
    def __init__(self, master):
        self.__master = master
        print(master)
        self.__window = Toplevel(self.__master)
        self.__frame = Frame(self.__window)
        self.__frame.pack(padx=500, pady=500)


