class A:
  __a=7;
  def fun(self):
   print(self.__a);

def main():
 obj=A();
 obj.fun();
 #print(obj.__a);      datahiding 
 print(obj._A__a);


main();
