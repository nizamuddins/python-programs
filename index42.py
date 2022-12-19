#  By in
# tuples
defTuples = ("apple","mango","banana");
for i in defTuples:
    print(i)
print(defTuples[2])
if "apple" in defTuples:
    print("true")

# set
newset = {1,3,2,4,7,4,3,6,7,4,};
for i in newset:
    print(i)
print(newset);
newset.add(0);
print(newset);
if 2 in newset:
    print("true")


# dictionary
defDic = {
    "name":"nizam",
    "age":21,
    "work":"student"
};

print(defDic);
print(defDic['name']);
defDic['name'] = "mohd";
print(defDic['name']);

for i in defDic:
    print(f'{i}:{defDic[i]}')

if 'name' in defDic:
    print("true")



