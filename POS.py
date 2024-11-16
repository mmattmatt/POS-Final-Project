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
            quantity = int(input(f"Quantity of {food}: "))
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
print("________________________")
print("YOUR CART:")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]} - Php.{prices[i]}")
print("------------------------")

for price in prices:
    total += price
print(f"Your total is: Php.{total}")
print("------------------------")

# Process 3 - PAYMENT
while True:
    cash_input = input("Enter your cash: ")
    print (f"You've entered Php.{cash_input}")
    print("________________________")
    try:
        cash = float(cash_input)
        if cash < total:
            print("Insufficient funds. Please try again.")
        elif cash > total:
            change = cash - total
            print(f"Your change is Php.{change}")
            break
        else:
            print("Exact amount. Thank you!")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
print("________________________")

#Receipt
print()
print ("****RECEIPT****")
