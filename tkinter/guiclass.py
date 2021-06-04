from tkinter import *

class Application(Frame):
 def __init__(self, master):
  super(Application, self).__init__(master)
  self.grid()
  self.create_widgets()

 def create_widgets(self):
  self.btn = Button(self, text = "I do nothing")
  self.btn.grid()

  self.btn2= Button(self)
  self.btn2.grid()
  self.btn2.configure(text = "Hhaha")

win = Tk()
win.title("Lazy Button 2")
win.geometry("200x200")

a = Application(win)

win.mainloop()
