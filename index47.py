# // By using regular expression
import re
string = "nizam is dev and";
s2 = re.sub("n","y",string);
print(s2);

s3 = s2.replace('y',"N");
print(s3)
