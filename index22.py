# program to find LCM by HCF

num1 = int(input("Enter the first number"));
num2 = int(input("Enter the Second number"));
hcf = 0;

for i in range(1,(num1+1 and num2+1)):
    if num1%i == 0 and num2%i == 0:
        hcf = i;

lcm = round((num1+num2)/hcf);

print(lcm)