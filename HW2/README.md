# Homework 2 Sample Problem

## Restaurant Ordering System

You have been hired to create an ordering system for a restaurant. The restaurant has a set menu with four different categories: drinks, appetizers, entrees, and desserts.

Create a list of the available items for each category. Make sure that each item category has at least 5 items available.

Your program should ask the customer what they would like to order from each category and check whether their choice is available at the restaurant.

**Hint:** Use `in` to check if the customer's choice is in the correct menu list.

For each category, the customer should first be asked what they would like. If their choice is available, add it to their order. If it is not available, tell the customer and give them one more opportunity to choose a different item.

If their second choice is also unavailable, automatically give them a default item.

The default items should be:

- Water for the drink
- Salad for the appetizer
- Pasta for the entree
- Ice cream for the dessert

The program should accept the customer's input regardless of capitalization.

**Hint:** Use `.lower()`.

Create a separate function for ordering from each of the four categories.

Finally, print the customer's completed order in a clear format and tell them that their order has been sent to the kitchen.

Organize your program using:

- A title docstring
- Your menu lists
- Function definitions
- An `if __name__ == "__main__":` block for the main program