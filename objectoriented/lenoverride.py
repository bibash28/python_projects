class Bibash:
 def __init__(self,cont):
  self.cont=cont;
  
 def __len__(self):
  return len(self.cont)*2;

a=Bibash([1,2,3,4]);
print(len(a));
