from tkinter import *

window=Tk()
window.geometry("400x300")
window.title("My first Tkinter window")


lbl=Label(text="Welcome",fg="blue",bg="yellow",width="30")
lbl.pack()
btn=Button(text="Click Me",bg="blue",fg="red")
btn.pack()
entry=Entry(fg="red",bg="yellow",width="50")
entry.pack()
text=Text(fg="blue",bg="orange",width="50")
text.pack()
frame=Frame(master=window,relief=RIDGE,borderwidth=5)
frame.pack()
lbl1=Label(master=frame,text="Frame Label")
lbl1.pack()
btn1=Button(master=frame,text="Frame button")
btn1.pack()
window.mainloop()