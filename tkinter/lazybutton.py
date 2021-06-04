from tkinter import *

win = Tk()
win.title("Lazy Buttons")
win.geometry("200x200")

#creating lazy buttons
cork = Frame(win)
cork.grid()

btn = Button(cork, text = "Click me")
btn.grid()

btn2 = Button(cork)
btn2.grid()

btn3 = Button(cork)
btn3.grid()
btn3["text"] = "Same here"

win.mainloop()
