# conversion of kilometers into miles

kilometers = int(input("Enter a kilometer value"));

# array = [char for char in kilometers];
factor = 0.6137;

miles = kilometers*factor;

print(f'{kilometers} is equals to {miles} miles')

# conversion of miles into kilometers

miles = int(input("Enter a kilometer value"));

# array = [char for char in miles];
factor = 0.6137;

kilometers = miles*factor;

print(f'{miles} is equals to {kilometers} kilometers')