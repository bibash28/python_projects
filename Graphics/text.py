from graphics import *

win = GraphWin("My Text", 1000, 1000)
win.setBackground("yellow")

#text
a = Text(Point(250,250), "Bibash") #center point 
a.draw(win)
a.setTextColor("red")
a.setStyle("bold")   #normal,italic,bold italic
a.setSize(25)        #font size
#a.setText("Goodbye")       #change the text
a.setFace("courier")     #font type

center = a.getAnchor()  #returns point
message =a.getText() #returns text


win.getMouse()
win.close()


