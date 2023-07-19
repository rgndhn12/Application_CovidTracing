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
scnd_label.pack(padx=1, pady=1)

scnd_entry = tk.Entry(top_2)
scnd_entry.pack(padx=1, pady=2)

thrd_label = tk.Label(top_2,text="Age:")
thrd_label.pack(padx=1, pady=4)

thrd_entry = tk.Entry(top_2)
thrd_entry.pack(padx=1, pady=6)

frth_label = tk.Label(top_2,text="Your Contact Number:")
frth_label.pack(padx=1, pady=8)

frth_entry = tk.Entry(top_2)
frth_entry.pack(padx=1, pady=10)

ffth_label = tk.Label(top_2,text="Person to contact in case of emergency:")
ffth_label.pack(padx=1, pady=12)

ffth_entry = tk.Entry(top_2)
ffth_entry.pack(padx=1, pady=14)

sxth_label = tk.Label(top_2,text="His/Her Contact Number:")
sxth_label.pack(padx=1, pady=16)

sxth_entry = tk.Entry(top_2)
sxth_entry.pack(padx=1, pady=18)

svth_label = tk.Label(top_2,text="Are you experiencing any symptoms of COVID-19 for the past 7 days?(Y/N):")
svth_label.pack(padx=1, pady=20)

svth_entry = tk.Entry(top_2)
svth_entry.pack(padx=1, pady=22)

sec_btn1 = tk.Button (top_2,text="Submit Entry")                 
sec_btn1.pack(padx=65, pady=65)

sec_btn2 = tk.Button (top_2, text="Back")
sec_btn2.pack(padx=70, pady=70)

top_2.mainloop()
