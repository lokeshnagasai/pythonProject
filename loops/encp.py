class myclass(object):
    def set_val(self,val):
        self.value=val

    def get_val(self):
        print(self.value)

a=myclass()
b=myclass()
a.set_val(100)
b.set_val(10000)
a.value=100# <== overriding set value directly.
#<== ie..  breaking encapsulation.

a.get_val()
b.get_val()