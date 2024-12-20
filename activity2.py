#import tkinter as tk
from tkinter import *

window=Tk()
window.title("My First Grid")
window.geometry("400x300")

for i in range(5):
    for j in range(5):
        frame=Frame(master=window,relief=RAISED,borderwidth=5)
        frame.grid(row=i,column=j,padx=5,pady=5)
        label=Label(master=frame,text=f"Row{i}\nColum{j}")
        label.pack()
window.mainloop()