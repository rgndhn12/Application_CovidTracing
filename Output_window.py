from tkinter import *

class OutputWindow:
    def __init__(self, master, output):
        self.__window = Toplevel(master)
        self.__output = output
        print(output)

        self.__window.mainloop()
    
    def make_output(self):

        self.__label = Label(self.__window)
        self.__label(text=self.__output)
        self.__label.pack()