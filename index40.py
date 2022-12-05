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


string2 = input("Enter a  string");
def myFunc(str):
    if("S").test(str) and ("G").test(str): 
        print("THe string starts with S and ends with G ")
    elif ("S").test(str):
      print("The string start with S but does not ends with G")
    elif ("G").test(str):
      print("The string  does not start with Sbut ends with G ")
    else:
      print(" THe string does not starts with S nither ends with G ")

myFunc(string2)


