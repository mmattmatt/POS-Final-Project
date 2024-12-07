# COMPUTER PROGRAMMING - FINAL PROJECT
# GROUP 8 - POINT OF SALES (POS)
# DEADLINE - DEC 11, 2024

foods = []
quantities = []
prices = []
total = 0
invalid_attempt_order_prompt = 0
invalid_attempt_food = 0
invalid_attempts_cash = 0
invalid_attempt_quantity = 0
invalid_attempt_choice = 0
max_payment = 25000
max_quantity = 50 
import sys
import datetime
import random

# Dictionary
menu_items = {
    "Fries": {"shortcut": "FR", "price": 25, "type": "food"},
    "Sandwich": {"shortcut": "SD", "price": 25, "type": "food"},
    "Muffin": {"shortcut": "MF", "price": 25, "type": "food"},
    "Hamburger": {"shortcut": "HB", "price": 30, "type": "food"},
    "Chicken": {"shortcut": "CC", "price": 60, "type": "food"},
    "ChocoCake": {"shortcut": "CH", "price": 65, "type": "food"},
    "HalfPizza": {"shortcut": "HP", "price": 135, "type": "food"},
    "Pizza": {"shortcut": "PZ", "price": 250, "type": "food"},
    "Milktea": {"shortcut": "MT", "price": 30, "type": "drink"},
    "Hot choco": {"shortcut": "HC", "price": 30, "type": "drink"},
    "Shake": {"shortcut": "SH", "price": 35, "type": "drink"},
    "Cold Brew": {"shortcut": "CB", "price": 45, "type": "drink"},
    "Espresso": {"shortcut": "ES", "price": 50, "type": "drink"}
}

# Process 1 - GET ORDER
print ("Hi there! 👋 Welcome to G8 Crave Cave!")
print ("Are you hungry? 🍔🍕 Craving something delicious? 😋 Let us know!")
# Step 1
while True:
    try:
        print ("[1] start".upper())
        print ("[2] exit".upper())
        choice = int(input("Enter your choice here: "))
        if choice == 1:
            break
        elif choice == 2:
            print ("Thank you for visiting. Please come again soon.")
            sys.exit()
        else:
            raise ValueError
    except ValueError:
        invalid_attempt_choice += 1
        print (f"Invalid input. Please select again. ({invalid_attempt_choice})")
        if invalid_attempt_choice == 3:
            print (f"You've reached the maximum (3) invalid attempts. Exiting...")
            sys.exit()

# Display Menu
print(r"""
╔──────────────────────────────────────────────╗
│  ___ ___    ___   _____    ___   ___   _____ │
│ / __| _ \  /_\ \ / / __|  / __| /_\ \ / / __|│
│| (__|   / / _ \ V /| _|  | (__ / _ \ V /| _| │
│ \___|_|_\/_/ \_\_/ |___|  \___/_/ \_\_/ |___|│
╚──────────────────────────────────────────────╝
""")
print("-"*48)
print("\t\t      Menu".upper())
print("-"*48)

print(("food:\t\t\t\t\tprice:").title())
for food, details in menu_items.items():
    if details["type"] == "food":
        print(f"{food} ({details['shortcut']})\t\t\t\tPhp {details['price']}")
print()
print("Drinks:")
for food, details in menu_items.items():
    if details["type"] == "drink":
        print(f"{food} ({details['shortcut']})\t\t\t\tPhp {details['price']}")
print("_"*48)

# Order Prompt
print()
while True:
    food_input = input("Enter a food to buy ('done' to quit): ")
    if food_input.lower() == 'done':
        if not foods:
            print("Your cart is empty. Please select an item to continue.")
            continue 
        else:
            break
        
    food_found = False
    for food, details in menu_items.items():
        if food_input.lower() == food.lower() or food_input.upper() == details['shortcut']:
            while True:
                try:
                    quantity = int(input(f"Quantity of {food}: "))
                    if quantity <= 0 or quantity >= max_quantity:
                        invalid_attempt_quantity += 1
                        print (f"Invalid quantity. Please try again. ({invalid_attempt_quantity})")
                        if invalid_attempt_quantity == 3:
                            print ("You've reached the maximum (3) invalid attempts. Exiting...")
                            sys.exit()
                    else: 
                        break
                except ValueError:
                    invalid_attempt_quantity += 1
                    print(f"Invalid input. Please enter a number. ({invalid_attempt_quantity})")
                    if invalid_attempt_quantity == 3:
                        print ("You've reached the maximum (3) invalid attempts. Exiting...")
                        sys.exit()

            price = details['price']
            foods.append(food)
            quantities.append(quantity)
            prices.append(price * quantity)
            food_found = True
            break

    if not food_found:
        invalid_attempt_food += 1
        print ("Invalid attempts:", invalid_attempt_food)
        if invalid_attempt_food == 3:
            print ("You've reached the maximum (3) invalid attempts. Exiting...")
            sys.exit()
        print("Invalid menu item. Please choose from the following:")
        for food, details in menu_items.items():
            print(f"- {food} ({details['shortcut']})")

# Process 2 - CART DISPLAY
print("_"*48)
print("YOUR CART:")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]}\t\t\t    - Php {prices[i]}")
print("-"*48)

for price in prices:
    total += price
print(f"Your total is: Php {total}")
print("-"*48)

# Process 3 - PAYMENT
while True:
    cash_input = input("Enter your cash: ")
    print("-"*48)
    try:
        cash = float(cash_input)
        invalid_attempts_cash += 1
        if cash > max_payment:
            print (f"You've reached the limit for payment. Please try again. ({invalid_attempts_cash})")
            if invalid_attempts_cash == 3:
               print ("You've reached the maximum (3) invalid attempts. Exiting...")
               sys.exit()
        elif cash < total:
            invalid_attempts_cash += 1
            print(f"Insufficient funds. Please try again. ({invalid_attempts_cash})")
            if invalid_attempts_cash == 3:
               print ("You've reached the maximum (3) invalid attempts. Exiting...")
               sys.exit()
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
        invalid_attempts_cash += 1
        print(f"Invalid input. Please enter a number. ({invalid_attempts_cash})")
        if invalid_attempts_cash == 3:
            print ("You've reached the maximum (3) invalid attempts. Exiting...")
            sys.exit()

print ("Generating a receipt.........\n")
print("-"*50)

# Process 4 - RECEIPT
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
print(r"""
╔──────────────────────────────────────────────╗
│  ___ ___    ___   _____    ___   ___   _____ │
│ / __| _ \  /_\ \ / / __|  / __| /_\ \ / / __|│
│| (__|   / / _ \ V /| _|  | (__ / _ \ V /| _| │
│ \___|_|_\/_/ \_\_/ |___|  \___/_/ \_\_/ |___|│
╚──────────────────────────────────────────────╝
""")
print("-"*50)
