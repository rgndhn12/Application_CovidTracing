# Dahan, Regine Fae M.      BSCPE 1-5    Covid Tracing App

#things included
    #ask user for information
    #write the colllected information in a file
    #add entry
    #search entry

import tkinter as tk

#window
top = tk.Tk()
top.geometry("1000x1000")
top.title (" COVID TRACING APP ")

main_label = tk.Label(top, text= " HEALTH MATTERS ", font=("Avenir",25)) 
main_label.pack(padx=30, pady=30)

main_btn1 = tk.Button (top, text="Add Entry")
main_btn1.pack(padx=100, pady=100)

main_btn2 = tk.Button (top, text="Search Entry")
main_btn2.pack(padx=300, pady=300)

top.mainloop()