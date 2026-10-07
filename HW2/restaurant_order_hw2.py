"""
Create a restaurant ordering system using the items available on the menu.
The program asks the customer to choose a drink, appetizer, entree, and dessert.
It checks if each choice is available, then gives the customer a second choice if necessary.
Then, it provides a default item if both choices are unavailable.
Finally, it prints their final order so that it can be sent to the kitchen to be prepared!
"""


# Create the restaurant menu

drinks = ["coke", "diet coke", "sprite", "dr pepper", "lemonade", "water", "iced tea"]

appetizers = ["wings", "nachos", "mozzarella sticks", "onion rings", "salad"]

entrees = ["burger", "cheeseburger", "steak", "cheesesteak", "pizza", "tacos", "pasta"]

desserts = ["ice cream", "apple pie", "brownie", "cookies", "chocolate cake"]


# Function to order a drink

def order_drink():
    first_choice = input("What drink would you like? ").lower()

    if first_choice in drinks:
        print(f"We have {first_choice}!")
        return first_choice

    else:
        print(f"Sorry, we do not have {first_choice}.")
        second_choice = input("Please choose another drink: ").lower()

        if second_choice in drinks:
            print(f"We have {second_choice}!")
            return second_choice

        else:
            print(f"Sorry, we do not have {second_choice} either.")
            print("We will add water to your order instead.")
            return "water"


# Function to order an appetizer

def order_appetizer():
    first_choice = input("What appetizer would you like? ").lower()

    if first_choice in appetizers:
        print(f"We have {first_choice}!")
        return first_choice

    else:
        print(f"Sorry, we do not have {first_choice}.")
        second_choice = input("Please choose another appetizer: ").lower()

        if second_choice in appetizers:
            print(f"We have {second_choice}!")
            return second_choice

        else:
            print(f"Sorry, we do not have {second_choice} either.")
            print("We will add salad to your order instead.")
            return "salad"


# Function to order an entree

def order_entree():
    first_choice = input("What entree would you like? ").lower()

    if first_choice in entrees:
        print(f"We have {first_choice}!")
        return first_choice

    else:
        print(f"Sorry, we do not have {first_choice}.")
        second_choice = input("Please choose another entree: ").lower()

        if second_choice in entrees:
            print(f"We have {second_choice}!")
            return second_choice

        else:
            print(f"Sorry, we do not have {second_choice} either.")
            print("We will add pasta to your order instead.")
            return "pasta"


# Function to order a dessert

def order_dessert():
    first_choice = input("What dessert would you like? ").lower()

    if first_choice in desserts:
        print(f"We have {first_choice}!")
        return first_choice

    else:
        print(f"Sorry, we do not have {first_choice}.")
        second_choice = input("Please choose another dessert: ").lower()

        if second_choice in desserts:
            print(f"We have {second_choice}!")
            return second_choice

        else:
            print(f"Sorry, we do not have {second_choice} either.")
            print("We will add ice cream to your order instead.")
            return "ice cream"


# Main program

if __name__ == "__main__":

    # Welcome the customer
    print()
    print("Welcome to our restaurant!")
    print("What would you like to have for dinner?")
    print()

    # Ask the customer for each part of their meal
    drink_order = order_drink()
    appetizer_order = order_appetizer()
    entree_order = order_entree()
    dessert_order = order_dessert()


    # Print the customer's final order
    print()
    print("Your final order is:")
    print(f"Drink: {drink_order}")
    print(f"Appetizer: {appetizer_order}")
    print(f"Entree: {entree_order}")
    print(f"Dessert: {dessert_order}")
    print()
    print("Your order has been sent to the kitchen!")