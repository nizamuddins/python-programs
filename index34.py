#to reverese a string

str = "nizam";
string = [char for char in str];
string.reverse();
str2 = "".join(string);
print(str2)

# --------------------

str3 ="";

for i in range(0,len(str)):
    str3 += str[len(str)-1-i];

print(str3)
    
