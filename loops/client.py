class Client:
    name="Lokesh"
    phone="8919643155"
    email="lokesh.mara2200@gmail.com"

def main():
    firstClient=Client()
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)
    firstClient.name="lokesh"
    firstClient.phone="8919643155"
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)


main()

