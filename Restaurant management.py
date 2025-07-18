# 🏨 PYTHON RESTAURANT ORDER SYSTEM

# Define the menu with items and their respective prices
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Greet the user and display the menu
print("Welcome to PYTHON RESTAURANT")
print("Pizza: BDT 40\nPasta: BDT 50\nBurger: BDT 60\nSalad: BDT 70\nCoffee: BDT 80\n")

# Initialize the total order cost
order_total = 0

# Ask the user to input their first order
item_1 = input('Enter the name of the item you want to order = ')
if item_1 in menu:
    order_total += menu[item_1]  # Add the price to the total
    print(f'Your item {item_1} has been added to your order')
else:
    print(f'Ordered item {item_1} is not available yet!')

# Ask the user if they want to add another item
another_order = input('Do you want to add another item? (Yes/No): ').lower()
if another_order == 'yes':
    item_2 = input('Enter the name of the second item = ')
    if item_2 in menu:
        order_total += menu[item_2]  # Add second item price
        print(f'Item {item_2} has been added')
    else:
        print(f'Ordered item {item_2} is not available!')

# Display the total amount to be paid
print(f'The total amount of items is to pay BDT {order_total}')
