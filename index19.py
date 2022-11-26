# program to find sum of natural numbres by for loop

numbers = int(input("Enter a number"));
sum = 0;
for i in range(0,numbers+1):
    sum = sum+i;

print(sum)