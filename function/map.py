def add(x):
 return x+5;

def main():
 a=[1,2,3,4,5,6];
 result=list(map(add,a));
 print(result);
 
 b=[9,8,7,6,5,4,3];
 result2=list(map(lambda x:x+5,b));
 print(result2);
main()




