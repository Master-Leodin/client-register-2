def menu():
    option = str(input("Choose a option, use the numbers\n1) Register a client\n2) See the client list\n3) Exit\n"))
    while option != "1" and option != "2" and option != "3":
        option = str(input("Choose a option, use ONLY this numbers\n1) Register a client\n2) See the client list\n3) Exit\n"))
    if option == "1":
        registration()
    elif option == "2":
        reg = open("customer.txt", "r")
        print(reg.read())
        reg.close
        menu()


def registration (reg = open("customer.txt", "a")):
    name = str(input("Write the client's name\n"))
    name = name.title()
    age = str(input("Write the client's age\n"))
    phone = str(input("Write the client's phone number\n"))
    
    txt = f"NAME = {name}, AGE = {age}, PHONE NUMBER = {phone}\n"
    
    reg.write(txt)
    reg.close
    question()


def question():
    option = str(input("Do you want to register another customer?\n1) Yes\n2) No\n"))
    while option != "1" and option != "2":
        option = str(input("Choose a option, use ONLY this numbers\n1) Yes\n2) No\n"))
    if option == "1":
        registration()
    elif option == "2":
        print("The program will restart to save the list")
