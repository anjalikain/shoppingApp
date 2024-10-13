import prduct_Catalogue

print("Welcome to the Demo Marketplace")
users = {
    "anjali": "P2",
    "admin": "1234",
    "U1": "5678",
    "U2": "P1"
}


def login():
    while True:
        print("Please enter username : ")
        username = input().lower()
        if username in users:
            print("Please enter  Password : ")
            password = input()
            if users[username] == password:
                print(f"Welcome, {username}!")
                break
            else:
                print("Incorrect password. Please try again")
        else:
            print("Incorrect Username")


login()
prduct_Catalogue.options_list()

