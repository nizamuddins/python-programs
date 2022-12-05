#  program to check occurence of char in string

string = input("Enter a string");
letter = input("Enter a letter to check");

occurence = string.count(letter);
print(occurence)
# ---------------
occurence2 = 0;

for i in range(0,len(string)):
   if string[i] == letter:
       occurence2 +=1;

print(occurence2);
