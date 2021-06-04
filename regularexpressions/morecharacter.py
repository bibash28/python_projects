import re;

a= r"egg(spam)*"; #  * - 0 or infinite repition
# a= r"egg(spam)+";  + - 1 or infinite repition  
# ? - 0 or 1 repitition
if re.match(a,"egg"):
 print("Match1");

if re.match(a,"eggspamspamegg"):
 print("Match2");


b = r"9{1,3}$"; # {,3}means 0 to 3            and         {0,} means 0 to infinite 
if re.match(b,"9"):
 print("Match3");
if re.match(b,"999"):
 print("Match4");
if re.match(b,"9999999999999999"):
 print("Match5");
else:
 print("No Match");



