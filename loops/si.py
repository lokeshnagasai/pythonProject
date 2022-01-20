class animal(object):
    def __init__(self, name):
        self.name=name

    def eat(self,food):
        print("%s is eating %s" % (self.name,food))

class dog(animal):
    def fetch(self,things):
        print("%s goes after the %s"%(self.name,things) )

class cat(animal):
    def swatstring(self):
        print("%s shared the string!"% self.name)

d=dog("tiger")
c=cat("chitteti")

d.fetch("ball")


