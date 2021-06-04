a=0;
b=1;


n=int(input("Enter the number of fibonacci number: "));
print(a);
print(b);
for i in range(1,n):
   c=a+b;
   print(c)
   a=b;
   b=c;

