import re;

pattern = r"(.+) \1";

if re.match(pattern,"spam spam"):
 print("Match1");

if re.match(pattern,"$5 $5"):
 print("Match2");

if re.match(pattern,"aa dd"):
 print("Match3");
else:
 print("No Match");




pattern =r"\D+\d";

# \d  = didgits
# \s = whitespace'
# \w = word characters
#big letters are opposite to small \D = non digits

#\b matches empty string
#\A  begining of string
# \Z end of string
