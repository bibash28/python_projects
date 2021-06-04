class A:
 def method1(self):
  print("A");

class B(A):
 def method2(self):
  print("B");
  
class C(B):
 def method3(self):
  print("C");

def main():
 c=C();
 c.method1();
 c.method2();
 c.method3();
 
main();
 
