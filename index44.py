#  By using copy method
import copy

dictionary = {
    'name':"nizam",
    "age":21
}
dictionary2 = {
    'name':"nzam",
    'age':23,
    "work":"student"
}


list1 = copy.deepcopy(dictionary2,dictionary);
print(list1)