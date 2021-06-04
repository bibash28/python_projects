from tkinter import *

class Application(Frame):
 def __init__(self,master):
  super(Application,self).__init__(master)
  self.grid()
  self.click = 0
  self.create_widget()

 def create_widget(self):
  self.btn1 = Button(self)
  self.btn1["text"] = "Total Clicks: 0"
  self.btn1["command"] = self.update
  self.btn1.grid()

 def update(self): 
  self.click+=1
  self.btn1["text"] = "Total Clicks:" +str(self.click) 


win = Tk()
win.title("Click Counter")
win.geometry("250x250")

a = Application(win)

win.mainloop()
