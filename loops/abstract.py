class MY_ABC_Class(object):
    def set_val(self,val):
        return
    def get_val(self):
        return
class MYClass(MY_ABC_Class):
    def set_val(self,input):
        self.val=input
    def hello(self):
        print("\nCalling the hello() method")
        print("im not part of the abstract method defined in my MY_ABC_class")

my_class=MYClass()
my_class.set_val(10)
print(my_class.get_val())
my_class.hello()



