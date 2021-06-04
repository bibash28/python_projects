import re;

a=r"a(bc)(de)(f(g)h)i";
#(b|c) either b or c


print(re.match(a,"abcdefghijklmnop").group());
print(re.match(a,"abcdefghijklmnop").group(0));
print(re.match(a,"abcdefghijklmnop").group(1));
print(re.match(a,"abcdefghijklmnop").group(2));
print(re.match(a,"abcdefghijklmnop").group(3));
print(re.match(a,"abcdefghijklmnop").groups());



pattern = r"(?P<first>abc)(?:def)(ghi)";
match = re.match(pattern,"abcdefghi");

if match:
 print(match.group());
 print(match.groups());
