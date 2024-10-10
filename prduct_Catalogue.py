import sys

import Payment

categories = {
    0: "Electronics",
    1: "Home Decor",
    2: "Kitchen",
    3: "Fashion"
}
product_categories = {
    "Electronics": {"Mobile", "Games", "Appliances", "TV"},
    "Home Decor": {"idols", "flowers", "painting"},
    "Kitchen": {"Cutlery", "Vegetable stand", "Jars", "lighter"},
    "Fashion": {"Clothes", "Shoes", "Watch", "Hats"}}


item = {}
global category


def choose_category():
    print("Please choose the product category by pressing a number : ")
    print("1: Electronics\n2: Home Decor\n3: Kitchen\n4: Fashion")
    global category

    while True:
        category = int(input())
        match category:
            case 1:
                print(product_categories["Electronics"])
                break
            case 2:
                print(product_categories["Home Decor"])
                break
            case 3:
                print(product_categories["Kitchen"])
                break
            case 4:
                print(product_categories["Fashion"])
                break
            case default:
                print("Please choose from above list : ")

    print("Wish to add product in your cart ? Y/N")
    ans = input().lower()
    if ans == "y":
        add_to_cart()
    elif ans == "n":
        while True:
            print("1. View Cart\n2. Add Product\n3. Payment\n4. Exit")
            user_choice = int(input())
            match user_choice:
                case 1:
                    view_cart()
                    break
                case 2:
                    choose_category()
                    break
                case 3:
                    Payment.total_amount()
                case 4:
                    print("Thank you")
                    sys.exit(0)
                case default:
                    print("Please choose from below list : ")
    else:
        print("Invalid input")
        choose_category()


def add_to_cart():
    print("Please enter product name : ")
    product = input()
    global item

    for key in product_categories.keys():
        if product in product_categories[key]:
            if key in item.keys():
                item[key].append(product)
            else:
                item[key] = [product]
            print("Wish to add more items? : Y/N")
            print("Electronics: TV,Appliances,Games,Mobile\n"
                  "Home Decor: painting,idols,flowers\n"
                  "Kitchen: lighter,Vegetable stand,Cutlery,Jars\n"
                  "Fashion: clothes,Shoes,Watch,Hats")
            user_choice = input().lower()
            if user_choice == "y":
                print("Same category ? Y/N")
                user_choice = input().lower()
                if user_choice == "y":
                    add_to_cart()
                elif user_choice == "n":
                    choose_category()
            else:
                options_list()


def view_cart():
    print("Current cart items : ", item)
    options_list()


def remove_from_cart():
    print("Do you wish to remove any item from your cart ? Y/N")
    user_choice = input().lower()
    if user_choice == "y":
        view_cart()
        print("Please enter product name : ")
        product = input()
        for key in product_categories.keys():
            if product in product_categories[key]:
                item[key].remove(product)
        remove_from_cart()
    else:
        print("Do you wish to go back to Main screen? Y/N")
        user_choice = input().lower()
        if user_choice == "y":
            choose_category()
        else:
            Payment.total_amount()


def options_list():
    while True:
        print("Please select from below options")
        print("1.Payment\n2.Add Product\n3.Exit")
        user_choice = int(input())
        match user_choice:
            case 1:
                Payment.total_amount()
                break
            case 2:
                choose_category()
                break
            case 3:
                print("Thank you")
                sys.exit(0)
