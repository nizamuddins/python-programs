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
    print("Not a pallindrome");
#--------------------------------

num1 = input("Enter a number");

length2 = len(num1);
temp2 = int(num1);
sum2 = 0;
while temp2 != 0:
    rem = temp2 % 10;
    val1 = rem ** length2;
    sum2 = sum2 + val1;
    temp2 = math.floor(temp2/10);

if sum2 == int(num1):
    print("It is pallindrome");
else:
    print("Not a pallindrome");
