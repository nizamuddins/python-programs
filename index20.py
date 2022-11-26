# program to check numbers has same last digit

num1 = int(input("Enter the first number"));
num2 = int(input("Enter the second number"));
num3 = int(input("Enter the third number"));

n1 = num1%10;
n2 = num2%10;
n3 = num3%10;

if n1==n2 and n1==n3:
    print("numbes has same last digits");
else:
    print("numbers doesn't has same last digits");
