#use function twice
def add_twice(fun,a):
 return fun(fun(a)); 

def add(x):
 return x+5;

a= add_twice(add,10);
print(a);

