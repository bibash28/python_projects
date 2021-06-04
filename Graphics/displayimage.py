from graphics import *

win = GraphWin("Image.jpg", 750, 750) #width,height
#win.setBackground(color_rgb(130, 0, 130))

a = Image(Point(400,600),"bibash.gif")
a.draw(win)
center = a.getAnchor()
width = a.getWidth()  #return in pixel
height = a.getHeight() #return in pixel;
red, green, blue = a.getPixel(32,18)
'''
returns a list RGB values of the pixel
at position x,y
'''
#a.setPixel(45,45, "blue")
a.save("bibash.ppm")


win.getMouse()
win.close()

