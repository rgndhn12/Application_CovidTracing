from tkinter import *

class SearchWindow:
    def __init__(self, master):
        self.__master = master
        print(master)
        self.__window = Toplevel(self.__master)
        self.__frame = Frame(self.__window)
        self.__frame.pack(padx=100, pady=100)

        self.make_form()

    def make_form(self):
        search_label = Label(self.__frame, text="Enter the submitted Name:")
        search_label.pack

        self.__search_entry = Entry(self.__frame)
        self.__search_entry.pack()

        search_btn = Button(self.__frame, text="Search", command=self.__search_entry)
        search_btn.pack()

    def search(self):
        contacts = []
        with open("user_contacts.txt") as user_contacts_file:
            for line in user_contacts_file:
                contacts.append(line.strip().split(',')) 
        print(f"Your searched entry:{contacts}")




        

