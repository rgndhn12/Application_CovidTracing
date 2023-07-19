# Dahan, Regine Fae M.      BSCPE 1-5    Covid Tracing App

import tkinter as tk

#window
top = tk.Tk()
top.geometry("500x500")
top.title (" COVID TRACING APP ")

frst_label = tk.Label(top, text= " Your Information... ", font=("Avenir",25)) 
frst_label.grid(row=2, column=3)

scnd_label = tk.Label(top,text="Full Name:")
scnd_label.grid(row=500, column=3)

thrd_label = tk.Label(top,text="Your Contact Number:")
thrd_label.grid(row=502, column=3)



frth_label = tk.Label(top,text="Person to call in case of emergency:")
frth_label.grid(row=504, column=3)

ffth_label = tk.Label(top,text="His/Her Contact Number:")
ffth_label.grid(row=506, column=3)

top.mainloop()
