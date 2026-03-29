class myClass2:
   def __method(self):
     print("This is a private method")
   def public_method(self):
        print("This is a public method")
        self.__method()  # Calling the private method from within the class

myObj=myClass2()
myObj.public_method()  # This will work fine
# myObj.__method()  # This will raise an AttributeError because __method is private


