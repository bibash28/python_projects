import re;




if re.match("spam","aspamspamspam"):
 print("Match");
else:
 print("No Match");




if re.search("spam","aaaspamaaspamaaaspam"):
 print("Match");
 print(re.search("spam","aaaspamaaspamaaaspam").group());
 print(re.search("spam","aaaspamaaspamaaaspam").start());
 print(re.search("spam","aaaspamaaspamaaaspam").end());
 print(re.search("spam","aaaspamaaspamaaaspam").span());
else:
 print("No Match");








print(re.findall("spam","aspamaaspamaaaspam"));
 

