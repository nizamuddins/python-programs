a = 3;
b = 5;


c = a;
a = b
b = c;

print(a);
print(b);

# -------------

num1 = 4;
num2 = 5;

num3 = num1+num2;
num1 = num3-num1;
num2 = num3-num2;

print(num1);
print(num2);
# -----------------------

n1 = 23;
n2 = 34;
[n1,n2] = [n2,n1];
print(n1);
print(n2);

# -------------------------
n3 = 3;
n4 = 6;

n5 = n3^n4;
n3 = n3^n5;
n4 = n4^n5;
print(n3);
print(n4);

