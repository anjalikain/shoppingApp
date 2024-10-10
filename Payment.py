# login using id- anjali ,password- 1234
# assuming the price of each product is Rs.10

import sys
import prduct_Catalogue
global amount


def make_payment():
    print("Your order is successfully placed")
    prduct_Catalogue.item = {}
    prduct_Catalogue.options_list()


def total_amount():
    global amount
    amount = 0

    for key in prduct_Catalogue.item:
        for i in range(len(prduct_Catalogue.item[key])):
            amount = amount + 10
    if amount == 0:
        print("Cart is empty")
        prduct_Catalogue.options_list()

    else:
        print("Total amount to be paid: ", amount)
        print("Please select payment method from below options")
        print("1. Net banking\n2.UPI\n3.Card")
        choice = input("Enter your choice: ")
        while True:
            match choice:
                case "1":
                    print("Proceed to net banking")
                    break
                case "2":
                    print("Proceed to UPI")
                    break
                case "3":
                    print("Proceed to Card payment")
                    break
                case default:
                    print("Please select payment method from above options")
                    choice = input()
    make_payment()






