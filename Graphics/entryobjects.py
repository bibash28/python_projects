from graphics import *

win = GraphWin("Entry Objects", 750, 750)
win.setBackground("green")

#entryobjects
inputBox = Entry(Point(125,125),20)   #centerpoint,width
inputBox.draw(win)
inputBox.setText("Enter Text")
inputBox.setFace("courier")       #font
inputBox.setSize(13)         #textsize 5 -> 36
inputBox.setStyle("italic")   #font style
inputBox.setTextColor("red")
center = inputBox.getAnchor()     #returns center
string = inputBox.getText()      #returns current string



win.getMouse()
win.close()



