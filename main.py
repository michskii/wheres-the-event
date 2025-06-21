from tkinter import *
window=Tk()
window.title("Event Handling")
window.geometry("100x100")
def event_handler(event):
    print(event.char)
window.bind("<Key>", event_handler)

def handle_click(event):
    print("\n the button has been clicked")
button=Button(text="click me")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()