import random;
import math
string = 'ACDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
string1 = math.floor(random.random()*len(string));
string2 = math.floor(random.random()*len(string));
string3 = math.floor(random.random()*len(string));
string4 = math.floor(random.random()*len(string));
string5 = math.floor(random.random()*len(string));

print(string[string1]+string[string2]+string[string3]+string[string4]+string[string5]);