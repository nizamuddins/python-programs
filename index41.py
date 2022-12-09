#program to find the anargramo of a string
def myfunc(x):
    x1= x.lower()
    x2 = [char for char in x1];
    x2.sort();
    x3 = "".join(x2);
    return x3;
    
def getIndexOfAnargram(s,w):
    result = [];
    for i in range(0,len(s)):
        x= slice(i,i+len(w));
        x2 = s[x];
        if myfunc(x2) == w:
            result.append(i);

    return result;


print(getIndexOfAnargram('cbaebabacd','abc'))    
