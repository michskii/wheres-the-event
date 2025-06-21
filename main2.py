from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")

def msg():
    messagebox.askokcancel("download", "download complete!")

button=Button(root, text="download", command=msg)
button.relief = "solid"
button.place(x=40, y=80)
root.mainloop()