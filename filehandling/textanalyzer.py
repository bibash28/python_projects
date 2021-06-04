def countchar(text,char):
   count=0;
   for i in text:
    if i==char:
     count+=1;
   return count;

with open("bibash.txt") as f:
#f= open("bibash.txt")
 print(f.read());
 print(countchar(f.read(),"r"));


