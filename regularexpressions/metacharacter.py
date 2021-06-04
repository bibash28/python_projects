import re;

# . - any character
# ^ - start of string
# $ - end of string
a = r".com";
#a=r"^.com$";
if re.match(a,"acom"):
 print("Match1");

if re.match(a,"bcom"):
 print("Match2");

if re.match(a,"aqcom"):
 print("Match3");
else:
 print("NoMatch");



aa = r"[a e i o u]";
if re.search(aa,"acom"):
 print("Match1");

if re.search(aa,"bcom"):
 print("Match2");

if re.search(a,"qcm"):
 print("Match3");
else:
 print("NoMatch");


aaa = r"[a-z][0-9]";
#aaa = r"[^a-z][^0-9]"; to invert
if re.search(aaa,"a6"):
 print("Match1");

if re.search(aaa,"b9"):
 print("Match2");

if re.search(aaa,"aqcom"):
 print("Match3");
else:
 print("NoMatch");



