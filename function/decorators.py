def printx():
 print("Hellow World");

def decorator(func):
 def wrap():
   print("-----------------");
   func();
   print("-----------------");
 return wrap;


#also can be used at any time
@decorator
def printy():
  print("Hello Bibash");

def main():
 decorator(printx)();
 printy();
 
main();
