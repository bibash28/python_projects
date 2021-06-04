#stringformatting
a="{}{}".format(1,2);
print(a);

b="{1}{0}".format(1,2);
print(b);

c="Bibash:{}{}{}".format(1,2,3);
print(c);

#join
d="1 2 3 4 5";
print("-".join(d))

#replace
e="mero nam k ho";
print(e);
print(e.replace("ho","ho?"));
#startswith
f="My name is Khan";
print(f.startswith("My"));
#endswith
print(f.endswith("Khaney"));
#upper
h="My name is Bibash";
print(h.upper());
#lower
print(h.upper().lower());
#split
i="My name is";
print(i.split(" "))

print("\n")
j= [1,2,3,4,5,6,7]
print(min(j));
print(max(j));
print(abs(-44));
print(sum(j));


