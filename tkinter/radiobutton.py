from tkinter import *
class Application(Frame):
 def __init__(self, cord):
  super(Application, self).__init__(cord)
  self.grid()
  self.create_widget()

 def create_widget(self):
  #create description label
  Label(self,
        text= "Choose your favourite movie type"
       ).grid(row=0, column=0, sticky=W)

  Label(self,
        text="Select one: "
       ).grid(row=1, column=0, sticky=W)

  #creating variable for single
  self.radio = StringVar()
  self.radio.set(None)

  #creating Comedy radio button
  Radiobutton(self,
               text="Comedy",
               variable= self.radio,
               value="comedy",
               command= self.update
               ).grid(row=2, column=0, sticky=W)
  Radiobutton(self,
              text="Drama",
              variable= self.radio,
              value="drama",
              command= self.update,
              ).grid(row=3, column=0, sticky=W)

  #create textfield  to display the text
  self.txt = Text(self,width=40, height=5, wrap=WORD)
  self.txt.grid(row=5, column=0, columnspan=3)

 #getting value
 def update(self):
  message =  "Your genre is "
  message+= self.radio.get()
  #clearing field and putting the message
  self.txt.delete(0.0,END)
  self.txt.insert(0.0,message)

win = Tk()
win.title("Radio Buton")
win.geometry("300x300")
#win.config(bg='blue')
a = Application(win)
win.mainloop()
