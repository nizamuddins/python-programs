# program to convert decimal to binary

def myFunc(n):
    if n<3:
        return n;
    else:
        return n*myFunc(n-1);

num = int(input("Enter a number?"));

fac = myFunc(num);

print(fac)