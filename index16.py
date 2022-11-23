# program to print fibonacci number

num = 5;

n1 = 0;
n2= 1;
nextTerm = 1;

for i in range(0,num):
    print(n1);
    nextTerm = n1+n2;
    n1 = n2;
    n2 = nextTerm;