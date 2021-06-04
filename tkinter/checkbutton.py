from tkinter import *

class Application(Frame):
 def __init__(self, cord):
  super(Application, self).__init__(cord)
  self.grid()
  self.create_widget()

 def create_widget(self):
  #creating label
  self.lbl = Label(self, text = "What do you want to eat?").grid(row=0, column=0, sticky=W)
  self.lbl2 = Label(self, text = "Select all that apply.")
  self.lbl2.grid(row=1, column=0, sticky=W)

  #creating the choices -> check button
  self.chkbtn1 = BooleanVar()      #only true or false
  Checkbutton(self,
              text = "Veg Momo",
              variable = self.chkbtn1,
              command = self.update
              ).grid(row=2, column=0, sticky=W)

  self.chkbtn2 = BooleanVar()      #only true or false
  Checkbutton(self,
              text = "Buff Momo",
              variable = self.chkbtn2,
              command = self.update
              ).grid(row=3, column=0, sticky=W)

  self.chkbtn3 = BooleanVar()      #only true or false
  Checkbutton(self,
              text = "Chicken Momo",
              variable = self.chkbtn3,
              command = self.update
              ).grid(row=4, column=0, sticky=W)

  #creating textfield
  self.txt = Text(self, width=40, height=5, wrap=WORD)
  self.txt.grid(row=5, column=0, columnspan=3)

 def update(self):
  a=""
  if self.chkbtn1.get():
   a+= "Good "
  if self.chkbtn2.get():
   a+= "excellent "
  if self.chkbtn3.get():
   a+= "Nice "
  self.txt.delete(0.0,END)
  self.txt.insert(0.0,a)

win = Tk()
win.title("Check Button")
win.geometry("250x250")
a = Application(win)
win.mainloop()
