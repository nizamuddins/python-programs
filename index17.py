import math;

num = '153';
length = len(num)
temp = int(num);
sum = 0;

while temp!=0:
    rem = temp%10;
    val = rem ** length;
    sum = sum+val;
    temp = math.floor(temp/10);

if sum == int(num):
    print("It is pallindrome");
else:
    print("Not a pallindrome")        