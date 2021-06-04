from tkinter import *

win = Tk()
win.title("Frame")
win.geometry("400x400")

#creating frame like cork in corkboard
a = Frame(win)
a.grid()

#creating label -> can be used in frame
b = Label(a, text ="This is my first text")
b.grid()

win.mainloop()


