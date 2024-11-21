# COMPUTER PROGRAMMING - FINAL PROJECT
# GROUP 8 - POINT OF SALES (POS)
# DEADLINE - DEC 11, 2024

foods = []
quantities = []
prices = []
total = 0

# Dictionary
menu_items = {
    "Fries": {"shortcut": "FR", "price": 25},
    "Sandwich": {"shortcut": "SD", "price": 25},
    "Muffin": {"shortcut": "MF","price": 25},
    "Hamburger": {"shortcut": "HB", "price": 30},
    "Chicken": {"shortcut": "CC", "price": 60},
    "ChocoCake": {"shortcut":"CH","price": 65},
    "HalfPizza": {"shortcut":"HP","price": 135},
    "Pizza": {"shortcut": "PZ", "price": 250},
    "Cookies": {"shortcut":"CK","price": 25},
    "Milktea": {"shortcut": "MT","price": 30},
    "Hot choco":{"shortcut": "HC","price": 30},
    "Shake": {"shortcut": "SH","price": 35},
    "Cold Brew":{"shortcut": "CB","price": 45},
    "Espresso": {"shortcut": "ES","price": 50}
}

# Process 1 - GET ORDER
print("Menu:")
for food, details in menu_items.items():
    print(f"{food} ({details['shortcut']})\t - Php {details['price']}")
    
print()
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
print("_"*25)
print("YOUR CART:")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]}\t - Php {prices[i]}")
print("-"*25)

for price in prices:
    total += price
print(f"Your total is: Php {total}")
print("-"*25)

# Process 3 - PAYMENT
while True:
    cash_input = input("Enter your cash: ")
    print("-"*25)
    try:
        cash = float(cash_input)
        if cash < total:
            print("Insufficient funds. Please try again.")
        elif cash > total:
            change = cash - total
            print (f"Received Php {cash_input}")
            print(f"Your change is Php {change:.2f}\n")
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
foramatted_datetime = now.strftime("%b. %d, %Y %I:%M %p")
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
    print(f"{quantities[i]} x {foods[i]} \t\t\t\t Php {prices[i]}\n")
print("-"*50)
# Footer
total_item_sold = sum(quantities)
print (f"ITEM COUNT:\t\t\t\t {total_item_sold}")
print (f"Subtotal:\t\t\t\t {total:.2f}\n")
print (f"GRAND TOTAL:\t\t\t\t {total:.2f}")
print (f"CASH:\t\t\t\t\t {cash:.2f}")
print (f"CHANGE:\t\t\t\t\t {change:.2f}")
print("-"*50)
# Message
print (f"\tTHANKS FOR CHOOSING {store_name.upper()}")
print ("\tWE HOPE TO SEE YOU AGAIN SOON!")
print("-"*50)
