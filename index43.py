import copy

list1 = [1,3,4,6];
list2 = copy.copy(list1);
list1[0] = 5;
list1.append("nizam")
print(list1);
print(list2);
list4 = [[1,4],[2,54]];
list5 = copy.deepcopy(list4);
print(list5);
list4[1][1] = 'AA';
print(list4);
print(list5);


