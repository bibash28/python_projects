class Animal:
 def __init__(self,name,color):
  self.name=name;
  self.color=color;

class Cat(Animal):
 def pur(self):
  print("Meow"); 

class Dog(Animal):
 def bark(self):
  print("Bark");


def main():
 a=Dog("Ema","Red");
 print(a.color);
 a.bark();
main();
