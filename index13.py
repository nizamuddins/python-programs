num = int(input("Enter a number?"));

flag = 0;

for i in range(2,num):
    if num%i==0:
        flag = 1;
        break;


if flag == 0 and num>1:
    print("number is  prime");
else:
    print("Number is not prime");    



num2 = 10;


for i in range(1,num2+1):
    flag1 = 0;
    for j in range(2,i):
        if i%j==0:
            flag1 = 1;
            break;

    if flag1 == 0 and i>1:
        print(i);
