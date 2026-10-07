# Burger Order Problem for Homework 1

WAGYU_PRICE = 14.08
BEEF_PRICE = 12.16
CHICKEN_PRICE = 11.20
VEGGIE_PRICE = 11.20
BRIOCHE_PRICE = 2.56
PRETZEL_PRICE = 2.56
SESAME_PRICE = 2.08
VEGGIE_WRAP_PRICE = 1.76

PLAIN_FRIES_PRICE = 6.08
SEASONED_FRIES_PRICE = 7.20
ONION_RINGS_PRICE = 5.60
SALAD_PRICE = 5.12

SODA_PRICE = 3.52
LEMONADE_PRICE = 3.04
WATER_PRICE = 0.00

MASS_TAX_RATE = 0.0625

customer_name = "Dan"

patty = "Beef"
patty_price = BEEF_PRICE

bun = "Brioche"
bun_price = BRIOCHE_PRICE

side = "Seasoned Fries"
side_price = SEASONED_FRIES_PRICE

drink = "Lemonade"
drink_price = LEMONADE_PRICE

subtotal = patty_price + bun_price + side_price + drink_price
tax = subtotal * MASS_TAX_RATE
total_before_discount = subtotal + tax

gift_card = 10.00
final_total = total_before_discount - gift_card

order_summary = (
    "WORCESTER BURGER ORDER \n"
    + "Customer: " + customer_name + "\n"
    + "Patty: " + patty + "\n"
    + "Bun: " + bun + "\n"
    + "Side: " + side + "\n"
    + "Drink: " + drink + "\n\n"
    + "Subtotal: $" + str(subtotal) + "\n"
    + "Tax: $" + str(tax) + "\n"
    + "Total before gift card: $" + str(total_before_discount) + "\n"
    + "Gift card: -$" + str(gift_card) + "\n"
    + "Final total: $" + str(final_total) + "\n"
)

print(order_summary)