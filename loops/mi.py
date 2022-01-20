class parent(object):
    def __init__(self, name):
        self.name=name

    def eat(self,food):
        print("%s is child of parent class " % (self.name , food))

class child(parent):
    def fetch(self,things):
        print("%s goes after the %s"%(self.name,things) )

class adopt(parent):
    def swatstring(self):
        print("%s shared the string!"% self.name)

d=child("class 2")
c=adopt("parent")

d.fetch("ball")



