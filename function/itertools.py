from itertools import count,accumulate,takewhile,permutations;

for i in count(3):
  print(i);
  if i>=11:
   break;

print(list(accumulate(range(10))));
print(list(takewhile(lambda x:x<5,[1,4,6,7,8])))
a= ("a","b","c")
print(list(permutations(a)));
