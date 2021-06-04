def fun():
 global a,b
 a = True
 b = False
 print(a,b)

def func():
 global a,b
 a = False
 b = True
 print(a,b)





a = False
b = True
print(a,b)
fun()
print(a,b)
func()
print(a,b)
