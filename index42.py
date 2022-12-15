#  By has_key()

class User():
    def __init__(self):
        self.name = "nizam";
        
obj = User();

if 'name' in obj:
    print('True')

