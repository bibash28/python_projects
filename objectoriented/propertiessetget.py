class Pizza:
 def __init__(self,topping):
  self.topping=topping;
  self._pineapple_allowed=False;

 @property
 def pineapple_allowed(self):
  return self._pineapple_allowed;

 @pineapple_allowed.setter
 def pineapple_allowed(self,value):
  if value:
   pas=input("Enter the password");
   if pas==3128:
    self._pineapple_allowed=value;
   else:
    raise ValueError("Incorrect");


def main():
 obj =Pizza(["cheese","tomato"]);
 print(obj.pineapple_allowed);
 obj.pineapple_allowed=True;
 print(obj.pineapple_allowed);


main();
