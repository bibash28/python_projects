from graphics import *

win = GraphWin("First Program", 1000, 1000)  #GraphWin(title, width, height)
win.setBackground('pink')
#win.setCoords(0,0,200,100) #-> to limit the range

#win.plotPixel(35, 128, "blue") ????????????????????

#constructing circle
c = Circle(Point(250,250), 150) #coordinate and radius of circle
c.draw(win)
c.setWidth(3)                   #width of circel outline
c.setOutline('red')
c.setFill('blue')
center =  c.getCenter()        #returns center
radius = c.getRadius()         #returns radius


#constructing point
p = Point(25,25)
p.draw(win)
x = p.getX()                   # returns x point
y = p.getY()                   # returns y point

#constructing line
line = Line(Point(20,50), Point(100,100))    # point 1 and point 2
line.draw(win)
line.setWidth(10)

line.setArrow("last")          #possible -> first, both
midpoint = line.getCenter()    #returns the midpoint of the line segment
startpoint = line.getP1()      #returns start point
endpoint = line.getP2()        #returns end point

win.getMouse()                 #waiting for mouse click to proceed
win.close()                    #closing window 

#constuctiong rectangle
rec = Rectangle(Point(1,3), Point(10,9))
rec.draw(win)
rec.setWidth(4)
rec.setOutline("brown")
rec.setFill("green")
