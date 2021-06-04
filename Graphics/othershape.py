from graphics import *

win = GraphWin("Shapes", 1000, 1000)
win.setBackground("pink")

#rectangle
rec = Rectangle(Point(100,100), Point(450,350))
rec.draw(win)
rec.setWidth(5)
rec.setFill("green")
rec.setOutline("brown")
center =  rec.getCenter()              #returns center
corner1 = rec.getP1()                   #returns first point to construct rec
corner2 = rec.getP2()                   #returns second point to construct rec

#oval
oval = Oval(Point(100,200), Point(450,650)) #boundind box
oval.draw(win)
oval.setWidth(3)
center =  oval.getCenter()              #returns center
corner1 = oval.getP1()                   #returns first point to construct rec
corner2 = oval.getP2()                   #returns second point to construct rec


#polygon
poly = Polygon(Point(100,2), Point(700,8), Point(150,355))      #points can be increased to increase sides
poly.draw(win)
poly.setWidth(5)
point = poly.getPoints()                       #return all points


win.getMouse()
win.close()
