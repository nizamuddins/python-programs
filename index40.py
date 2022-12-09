# starWith() and endWith() method

string = input("Enter a  string");

def myFunc(str):

    if str.startswith("S") and str.endswith("G"):
        print("THe string starts with S and ends with G")
    elif str.startswith("S"):
        print("The string start with S but does not ends with G")
    elif str.endswith("S"):
        print("The string  does not start with S but ends with G")
    else:
        print("THe string does not starts with S nither ends with G")


myFunc(string)
