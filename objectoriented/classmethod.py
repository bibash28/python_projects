class Rectangle:
 def __init__(self,width,height):
  self.width=width;
  self.height=height;

 def area(self):
  return self.width*self.height;

 @classmethod
 def newsquare(cls,sidelength):
  return cls(sidelength,sidelength);



def main():
 a = Rectangle.newsquare(5);
 b = a.area();
 print(b); 




main();
