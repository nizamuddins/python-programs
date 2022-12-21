# // program to convert an dictionary to a jsonString
import json

dic = {
    'name':'nizam',
    'age':21
}
x = json.dumps(dic);
print(x);

# // program to convert an jsonString to dictionary.

jsonStr = "{'name':'nizam','age':21 }"
x2 = json.loads(jsonStr);
print(x2);