class User():
    def __init__(self,name,age,work):
            self.name=name
            self.age=age
            self.work=work
            self.arr = ['nziam',"bad"]
    def myfunc(self):
        print("I am back")
            

obj = User("nizam",21,'student');
print(obj.name);
obj.myfunc();
print(obj.arr);

del obj.name;
del User.myfunc;

