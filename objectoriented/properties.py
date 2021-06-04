class Pizza:
 def __init__(self,topping):
  self.topping=topping;

 @property
 def pine_allow(self):
  return False;

def main():
 b=Pizza(["cheese","tomato"]);
 print(b.pine_allow);
 b.pine_allow=True;


main();
