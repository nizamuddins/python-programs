# program to print fibonacci sequence by recurrsipn

num = int(input("Enter a Number"));

def fibonacci(n):
    if n<2:
        return n;
    else:
        return fibonacci(n-1)+fibonacci(n-2);    



 
for i in range(0,num):
     print(fibonacci(i));
     