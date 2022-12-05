#To sort string in alphabetical order
str = input("Enter a string");
split = [char for char in str];

split.sort();
print(split)
for x,i in enumerate(split):
    print(i);
