# program to guess random number

import random;
import math;

num = math.floor(random.random()*10)+1;

def myfunc():
    number = int(input("Guess a number"));
    print(num)
    if num == number:
        print("You won");
    else:
         myfunc();   
myfunc()