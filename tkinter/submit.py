from tkinter import *

class Application(Frame):
 def __init__(self, master):
  super(Application, self).__init__(master)
  self.create_widget()
  self.grid()

 def create_widget(self):
  #create instruction label
  self.lbl = Label(self, text = "Enter password to access")
  self.lbl.grid(row=0, column=0, columnspan=2, sticky=W)

  #create password label
  self.lbl2 = Label(self, text = "Password: ")
  self.lbl2.grid(row=1, column=0, sticky=W)

  #create the entry box
  self.box = Entry(self)
  self.box.grid(row=1, column=1, sticky=W)

  #create button
  self.btn = Button(self, text = "Submit", command = self.action)
  self.btn.grid(row=2, column=0, sticky=W)

  #create text widget
  self.txt = Text(self, width=35, height=5, wrap=WORD)
  self.txt.grid(row=3, column=0, columnspan=2, sticky=W)

 def action(self):
  #display message based on password
  message = self.box.get()
  if message == "3128":
    a = "You are the elder brother"
  elif message == "7068":
    a = "You are younger brother"
  #first delete any text already in the string
  self.txt.delete(0.0,END)
  #insert message
  self.txt.insert(0.0,a)

win = Tk()
win.title("Longevity")
win.geometry("450x450")

a = Application(win)

win.mainloop()
