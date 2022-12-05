#To find string is pallindrome or not
str = input("Enter a string");

def pallinfrome(string):
    flag = 0;
    length = len(string)
    for i in range(0,length):
        if string[i]==string[length-1-i]:
            flag = 0;

        else:
            flag = 1;
    if flag == 0:
        print("Strinfg is pallindrome");
    else:
        print("Not a pallindrome")    
                
pallinfrome(str); 
