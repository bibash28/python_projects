a=open("bibash.txt","r");
b=a.read();
print(b);


#16 represents byte
print(a.read(16));
print(a.read(4));
print(a.read());
a.close();
