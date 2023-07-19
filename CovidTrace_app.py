# Dahan, Regine Fae M.      BSCPE 1-5    Covid Tracing App

#things included
    #ask user for information
    #write the colllected information in a file
    #add entry
    #search entry

import tkinter as tk

# main window

top = tk.Tk()
top.geometry("1000x1000")
top.title (" COVID TRACING APP ")
bg_img = tk.PhotoImage(file="C:\\Users\\USER\\Documents\\OOP Second Sem\\CTracing_App\\imgbg.png")
tk.Label(top, image=bg_img).pack()
top['background'] = 'black'

main_label = tk.Label(top, text= " HEALTH MATTERS ", font=("Arial",40),
                      bg="black",fg="Pink")
main_label.pack(padx=30, pady=30)

main_btn1 = tk.Button (top,text="Add Entry")                 
main_btn1.pack(padx=50, pady=50)


main_btn2 = tk.Button (top, text="Search Entry")
main_btn2.pack(padx=100, pady=100)

top.mainloop()