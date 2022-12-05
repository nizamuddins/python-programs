string = input("Enter a string");

def myfunc(args):
    x = slice(0,1);
    y = args[x].upper();
    z = args.replace(args[0],y);
    return(z)
ret = myfunc(string);    
print(ret);
