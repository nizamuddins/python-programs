#  By using copy method
import copy

dictionary = {
    'name':"nizam",
    "age":21
}
dictionary2 = {
    'name':"nzam",
    'age':23,
    "work":['nizma']
}


list1 = copy.deepcopy(dictionary2);
print(list1)