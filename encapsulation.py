class myClass:
    x=10
    __y=20
    def display(self):
     print(self.__y)


myObj=myClass()
print(myObj.x)
myObj.display()  