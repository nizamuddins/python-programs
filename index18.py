num1 = int(input("Enter a number"));
num2 = int(input("Enter a number"));

sym = input("Enter a operator");

if sym == "+":
    print(num1+num2);
elif sym == "-":
    print(num1-num2);
elif sym == "*":
    print(num1*num2);
elif sym == "/":
    print(num1/num2);
else:
    print(num1%num2);
