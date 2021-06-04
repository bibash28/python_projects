from graphics import *

window = GraphWin("House",400,400)

tri = Polygon(Point(20,70), Point(60,30), Point(100,70))
tri.draw(window)

parm = Polygon(Point(60,30), Point(100,70), Point(360,70), Point(320,30))
parm.draw(window)
parm.setFill('white')

rec1 = Rectangle(Point(20,70),Point(100,200))
rec1.draw(window)
rec1.setFill('red')

rec11 = Rectangle(Point(50,135),Point(70,200))
rec11.draw(window)
rec11.setFill('grey')

rec2 = Rectangle(Point(100,70),Point(360,200))
rec2.draw(window)
rec2.setFill('blue')

for i in range(1,160,40):
 rec22 = Rectangle(Point(150+i,110),Point(190+i,160))
 rec22.draw(window)
 rec22.setFill('brown')
line1 = Line(Point(150,135),Point(310,135))
line1.draw(window)


window.getMouse()
window.close()


