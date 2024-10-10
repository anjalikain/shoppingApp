import sys

import Payment

categories = {
    0: "Electronics",
    1: "Home Decor",
    2: "Kitchen",
    3: "Fashion"
}
product_categories = {
    "Electronics": {"mobile", "games", "appliances", "tv"},
    "Home Decor": {"idols", "flowers", "painting"},
    "Kitchen": {"cutlery", "vegetable stand", "jars", "lighter"},
    "Fashion": {"clothes", "shoes", "watch", "hats"}}


item = {}
global category


def choose_category():
    print("Please choose the product category by entering a number(1-4) : ")
    print("1: Electronics\n2: Home Decor\n3: Kitchen\n4: Fashion")
    global category

    while True:
        category = input()
        if is_integer(category):
            match category:
                case '1':
                    print(product_categories["Electronics"])
                    break
                case '2':
                    print(product_categories["Home Decor"])
                    break
                case '3':
                    print(product_categories["Kitchen"])
                    break
                case '4':
                    print(product_categories["Fashion"])
                    break
                case default:
                    print("Please choose from above list : ")
        else:
            print("Please enter a valid number")

    print("Wish to add product in your cart ? Y/N")
    ans = input().lower()
    if ans == "y":
        add_to_cart()
    elif ans == "n":
        options_list()
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
    else:
        print("Please enter correct product name")
        add_to_cart()


def view_cart():
    if len(item) == 0:
        print("Cart is empty")
    else:
        print("Current cart items : ", item)
    options_list()


def remove_from_cart():
    found = False
    print("Do you wish to remove any item from your cart ? Y/N")
    user_choice = input().lower()
    if user_choice == "y":
        print("Please enter product name : ")
        product = input()
        for key, value_list in item.items():
            if product in value_list:
                found = True
                break
        if not found:
            print("item doesn't exist")
            options_list()
        for key in product_categories.keys():
            if product in product_categories[key]:
                item[key].remove(product)
                print("item removed")
                remove_from_cart()
            else:
                continue
        else:
            print("Please enter correct item name")
    else:
        options_list()


def options_list():
    while True:
        print("Please enter a number(1-5) to select from below options")
        print("1.View Cart\n2.Remove product from cart\n3. Add product\n4.Payment\n5.Exit")
        user_choice = input()
        if is_integer(user_choice):
            match user_choice:
                case '1':
                    view_cart()
                    break
                case '2':
                    remove_from_cart()
                    break
                case '3':
                    choose_category()
                    break
                case '4':
                    Payment.total_amount()
                    break
                case '5':
                    print("Thank you")
                    sys.exit(0)


def is_integer(user_choice):
    try:
        int(user_choice)
        return True
    except ValueError:
        return False

