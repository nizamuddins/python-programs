class User():
    def __init__(self,name,age,work):
            self.name=name
            self.age=age
            self.work=work
    def myfunc(self):
        print("I am back")
            

obj = User("nizam",21,'student');
print(obj.name);
obj.myfunc();


