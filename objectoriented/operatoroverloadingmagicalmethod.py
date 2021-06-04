++++++++++++++
class Vector:
 def __init__(self,x,y):
  self.x=x;
  self.y=y;
 def __add__(self,z):
  return Vector(self.x+z.x , self.y+z.y);


def main():
 a= Vector(1,2);
 b= Vector(3,4);
 result=a+b;
 print("("+str(result.x)+","+str(result.y)+")");
 

main();
