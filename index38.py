string = input("Enter a string");
def myfunc(args):
    length=0;
    length += args.count("a");
    length += args.count("e");
    length += args.count("i");
    length += args.count("o");
    length += args.count("u");
    return length;

ret = myfunc(string);
print(ret)
    