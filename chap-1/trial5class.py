class dog:
    def bark(self):
        print("wow wow")
mydog=dog()
mydog.bark()           
#let's do some cat
# 
class cat:
    def bark(self, str):
        print("meow" + str)
mycat=cat()
mycat.bark("ksss")

#let's manipulate some shit

class dinosour:
    def __init__(self, name="", age=0, color="", spine=""):
        self.name=name
        self.age=age
        self.color=color   
        self.spine=spine
newdinosour=dinosour("pinky", 12, "red", "swiggly")
print(newdinosour.name)