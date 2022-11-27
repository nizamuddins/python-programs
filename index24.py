# program to find sum of a number

num =15;

def myfunc(n):
    if n>0:
        return n+myfunc(n-1) 
    else:
        return n;


num2 = myfunc(num);

print(num2)