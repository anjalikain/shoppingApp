
Introduction

This technical design document outlines the design and functionality of a Shopping Application. The system allows users to log in, browse various product categories, add items to a shopping cart, manage the cart, and process payments. The goal of this document is to provide a detailed overview of the system architecture, modules, and design choices.

System Overview

The shopping application is a simple, command-line-based system that implements core shopping functionalities, including:

•	User Authentication
•	Product Catalogue and Categories
•	Cart Management
•	Payment System

The program is developed using Python, focusing on object-oriented and modular programming. It uses external modules (prduct_Catalogue, Payment), which provide product listings and payment handling functionality.

 Key Functionalities:
•	User login and session management
•	Dynamic product browsing by category
•	Cart management (add/remove/view products)
•	Payment processing with multiple payment options
Modules and Functionality
User Authentication
The authentication module allows users to log in with predefined usernames and passwords.

Function: login()
•	Purpose: Authenticate the user by prompting for a username and password.
•	Process: 
o	The system checks if the entered username exists in the `users` dictionary.
o	If the username exists, it prompts for the password and checks its validity.
o	On successful authentication, the user is granted access; otherwise, they are prompted to re-enter credentials.










Product Catalogue
The product catalog organizes products into different categories and allows users to browse and select items.

Function: choose_category()
•	Purpose: Let the user select a product category from a predefined list and view the available items.
•	Process:
o	Displays the available product categories.
o	Upon selection, lists the items in the chosen category.
o	Allows the user to add items from the selected category to the cart.









Categories Dictionary:














Shopping Cart
The shopping cart module allows users to manage the items they wish to purchase.

Function: add_to_cart()
•	Purpose: Add selected items to the shopping cart.
•	Process: 
o	Allows users to input a product name.
o	Checks if the product is valid (exists in the catalog) and adds it to the `item` dictionary.
  
Function: view_cart()
•	Purpose: Display all the items currently in the cart.

Function: remove_from_cart()
•	Purpose: Remove a product from the cart.
•	Process:
o	Prompts the user for the product to remove.
o	Checks if the product exists in the cart and removes it.


Shopping Cart Structure:




Payment System
The payment system handles the checkout process.

Function: total_amount()
•	Purpose: Calculate the total amount to be paid based on the items in the cart.
•	Process:
o	Assumes each item has a price of ₹10.
o	Displays the total amount.
o	Prompts the user to select a payment method (Net Banking, UPI, or Card).

Function: make_payment()
•	Purpose: Finalizes the order and resets the cart after successful payment.












Flow Diagrams

User Flow
•	User logs in via the login() function.
•	After successful login, the user selects an option (view cart, add products, remove products, proceed to payment).
•	If "Add Product" is selected, the user selects a category and adds items to the cart.
•	The user can then view the cart or proceed to payment.
•	Upon choosing payment, the total is calculated, and the user is prompted to select a payment method.
•	After payment, the cart is reset, and the user can exit the program.

Payment Flow
•	total_amount() is called.
•	The total cost of all items in the cart is calculated.
•	User selects a payment method (Net banking, UPI, or Card).
•	Upon successful selection, make_payment() is invoked, placing the order.


External Dependencies

•	prduct_Catalogue: Manages the list of available products and categories.
•	Payment: Manages the payment handling logic (amount calculation and order finalization).

Both modules are external dependencies that should be developed or mocked in the system.

Error Handling and Edge Cases

•	Invalid Username/Password: Handled by continuously prompting the user for valid credentials in the `login()` function.
•	Invalid Category/Product Selection: The system prompts the user to enter valid input when incorrect product or category names are provided.
•	Empty Cart: If the cart is empty, the user is notified when trying to proceed to payment or view the cart.
Future Enhancements

•	Object-Oriented Design: Refactor the application into an object-oriented design for better scalability and modularity.
•	Database Integration: Store user credentials, product data, and transaction history in a database.
•	Pricing Model: Implement a dynamic pricing model instead of fixed prices (₹10 per product).
•	UI/UX Improvements: Move from a command-line interface to a web-based or GUI-based system using frameworks like Flask or Django.
•	Enhanced Security: Add encryption for user credentials and secure payment options.


Conclusion:
This document outlines the current state of the shopping application, its functionality, and possible future enhancements. The design is structured to be modular and extendable, allowing future integration of additional features and improvements.
