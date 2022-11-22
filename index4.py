import math
a = int(input("enter a value"));
b = int(input("enter a value"));
c = int(input("enter a value"));

s = (a + b + c) / 2


area = round(math.sqrt(s*(s - a) * (s - b) * (s - c)),2);
print(area)


#base ansd height
height = 21;
base = 32;

area2 = round((base * height)/2,2);
print(area2)