from graphics import *
window = GraphWin("DDA line diagram",400,400)

def dda(x1,y1,x2,y2):
 dx = x2 - x1
 dy = y2 - y1
 if abs(dx) > abs(dy):
  stepsize = dx
 elif abs(dx) < abs(dy):
  stepsize = dy
 x_inc = dx/stepsize
 y_inc = dy/stepsize
 x_new = x1
 y_new = y1
 
 for i in range(1,stepsize+1): 
  x_old = x_new
  y_old = y_new
  x_new = x_new + x_inc  
  y_new = y_new + y_inc
  print(x_new,y_new)
  Line(Point(x_old,y_old),Point(x_new,y_new)).draw(window)
  i+=1



dda(10,10,10,380)
dda(10,380,380,380)

dda(40,170,150,130)
dda(150,130,240,135)
dda(240,135,330,165)

  


 





window.getMouse()
window.close()
