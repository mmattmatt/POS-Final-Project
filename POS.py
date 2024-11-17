# COMPUTER PROGRAMMING - FINAL PROJECT
# GROUP 8 - POINT OF SALES (POS)
# DEADLINE - DEC 11, 2024

foods = []
quantities = []
prices = []
total = 0

#dictionary
menu_items = {
    "Hamburger": {"shortcut": "HB", "price": 60},
    "Chicken": {"shortcut": "CC", "price": 120},
    "Fries": {"shortcut": "FR", "price": 45},
    "Pizza": {"shortcut": "PZ", "price": 300},
    "Chicken Sandwich": {"shortcut": "CS", "price": 80}
}
# Process 1 - GET ORDER
print("Menu:")
for food, details in menu_items.items():
    print(f"{food} ({details['shortcut']}) - Php.{details['price']}")

while True:
    food_input = input("Enter a food to buy ('done' to quit): ")
    if food_input.lower() == 'done':
        break

    food_found = False
    for food, details in menu_items.items():
        if food_input.lower() == food.lower() or food_input.upper() == details['shortcut']:
            while True:
                try:
                    quantity = int(input(f"Quantity of {food}: "))
                    if quantity <= 0:
                        print ("Please select again")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number")

            price = details['price']
            foods.append(food)
            quantities.append(quantity)
            prices.append(price * quantity)
            food_found = True
            break

    if not food_found:
        print("Invalid menu item. Please choose from the following:")
        for food, details in menu_items.items():
            print(f"- {food} ({details['shortcut']})")

# Process 2 - CART DISPLAY
print("_"*24)
print("YOUR CART:")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]} - Php.{prices[i]}")
print("-"*24)

for price in prices:
    total += price
print(f"Your total is: Php.{total}")
print("-"*24)

# Process 3 - PAYMENT
while True:
    cash_input = input("Enter your cash: ")
    print (f"You've entered Php.{cash_input}")
    print("-"*24)
    try:
        cash = float(cash_input)
        if cash < total:
            print("Insufficient funds. Please try again.")
        elif cash > total:
            change = cash - total
            print(f"Your change is Php.{change}\n")
            break
        else:
            print("Exact amount.\n")
            change = 0
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
print ("Generating a receipt.........\n")
print("-"*50)

# Process 4 - RECEIPT
import datetime
import random
# Store information
store_name = ("g8 crave cave")
store_address = ("bulacan state university")
cashier_names = ["Mask", "Liance", "Aries"]
random_cashier = random.choice(cashier_names)
# Date and time
now = datetime.datetime.now()
foramatted_datetime = now.strftime("%b. %d, %Y %I:%M:%S %p")
# Header
print ("\t\t OFFICIAL RECEIPT")
print ("*"*50)
# Body
print (f"{store_name.title()}")
print (f"{store_address.title()}")
print (f"Cashier: {random_cashier}")
print (f"{foramatted_datetime}\n")
print("ITEM(S):\n")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]} \t\t\t\t Php.{prices[i]}\n")
print("-"*50)
# Footer
total_item_sold = sum(quantities)
print (f"NO. OF ITEMS:\t\t\t\t {total_item_sold}")
print (f"Subtotal:\t\t\t\t Php.{total}\n")
print (f"GRAND TOTAL:\t\t\t\t Php.{total}")
print (f"CASH:\t\t\t\t\t Php.{cash}")
print (f"CHANGE:\t\t\t\t\t Php.{change}")
print("-"*50)
# Message
print (f"\tTHANKS FOR CHOOSING {store_name.upper()}")
print ("\tWE HOPE TO SEE YOU AGAIN SOON!")
print("-"*50)