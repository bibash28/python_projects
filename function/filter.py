a=[1,2,3,4,5,6,7,8,9,10,11,12];
print(a);
print("Filtering multiple of 3");
result= list(filter(lambda x:x%3==0,a));
print(result);
