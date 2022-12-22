# // By .includes() method

string = "I am nizam from Liet";

target ="zam";

if string.__contains__(target):
    print("The string contains "+ target);
else:
    print("The string does not contains "+ target);

# // By rfind() method

string1 = " Nizam developer from home";
strCheck1 = 'dev';

result  = string1.rfind(strCheck1);
if result != -1:
    print("The string contains "+ strCheck1);

else:
    print("The string does not contains "+ strCheck1);
