# Dahan, Regine Fae M.      BSCPE 1-5    Covid Tracing App

import tkinter as tk

#second window
top_2 = tk.Tk()
top_2.geometry("1000x1500")
top_2.title (" COVID TRACING APP ")
top_2['background'] = 'black'

frst_label = tk.Label(top_2, text= " YOUR INFORMATION... ", font=("Avenir",25)) 
frst_label.pack(padx=30, pady=30)

scnd_label = tk.Label(top_2,text="Full Name:")
scnd_label.pack(padx=5, pady=40)

thrd_label = tk.Label(top_2,text="Age:")
thrd_label.pack(padx=5, pady=41)

frth_label = tk.Label(top_2,text="Your Contact Number:")
frth_label.pack(padx=5, pady=42)

ffth_label = tk.Label(top_2,text="Person to contact in case of emergency:")
ffth_label.pack(padx=5, pady=43)

sxth_label = tk.Label(top_2,text="His/Her Contact Number:")
sxth_label.pack(padx=5, pady=44)

svth_label = tk.Label(top_2,text="Are you experiencing any symptoms of COVID-19 for the past 7 days?(Y/N):")
svth_label.pack(padx=5, pady=45)

sec_btn1 = tk.Button (top_2,text="Submit Entry")                 
sec_btn1.pack(padx=65, pady=65)

sec_btn2 = tk.Button (top_2, text="Back")
sec_btn2.pack(padx=70, pady=70)

top_2.mainloop()
