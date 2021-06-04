#list
a=[1,2,3,4];
print(a);
print(a[2]);
#length
print(len(a));

#add
a.append(5);
print(a);
a.remove(4);
print(a);
print(a[1]);
#last element
print(a[-1]);

#print slice
print(a[0:4]);
#begins from first
print(a[:4]);
#goes upto last
print(a[0:]);
print(a[4:1:-1]);

#add at any place add in 3rd place 4
a.insert(3,4);
print(a);


print("lol");
#give position of content in the list
print(a.index(3));

#to take range of values
x= list(range(10));
print(x);
print(list(range(6,9)));
print(list(range(1,100,5)));
#from last
print(list(range(100,1,-5)));


#list comprehension
cube = [i**3 for i in range(5)];
print(cube);

#withconditions
evens=[i**2 for i in range(10) if i**2%2==0];
print(evens);

num=[11,22,33,445,55];
cond=[i>5 for i in num];
if all(cond):
 print("All above 5");
if any([i>100 for i in num]):
 print("At least one above 100");

for v in enumerate(num):
  print(v);
