class person:
    name="i have no name"
    def sayname(self):
        print("my name is ...Lokesh",self.name)

def main():
    aperson=person()
    aperson.sayname()
    aperson.name="big smiely d"
    aperson.sayname()

main()
