import math
a = 3;
b= 7;
c = 2;

p = b * b - 4 * a * c;
p = -4;

if p>0:
    root1 =round((-b + math.sqrt(p))/(2*a),2);
    root2 =round((-b - math.sqrt(p))/(2*a),2);
    print(f"roots g are {root1},{root2}")
elif p == 0:
    root1 = root2 = (-b)/(2*a);
    print(f"roots are {root1},{root2}")

else:
    img = (-b)/(2*a);
    real = round(math.sqrt(-(p))/(2*a),2);
    print(f"Roots of quadratic equation is {img}+{real}i and {img}-{real}i")
