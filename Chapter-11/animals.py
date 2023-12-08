class Animals:
    def __init__(self):
        print( "i am an Animal class")


class Pets(Animals):
    def __init__(self):
        print("i am pet class and i have inherited from animal class")

class Dogs(Pets):
    def __init__(self):
        super().__init__()
        print( "i am a dog class and my parent class is Pets and pets's parent class is animal")
    
    def bark(self):
        return "i make a sound - boo boo"


a = Animals()
p  = Pets()
d = Dogs()
print(d.bark())