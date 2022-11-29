#program to convert decimal to binary
import math;

num = int(input("Enter a Number?"));

bin =0;
i = 1;
temp = num;

while temp != 0:
    rem = temp%2;
    bin = bin+rem*i;
    i = i*10;
    temp = math.floor(temp/2)

print(bin)