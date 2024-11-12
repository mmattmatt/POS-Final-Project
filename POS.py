foods = []
quantities = []
prices = []
total = 0

print("Menu:")
print("Hamburger - Php.50")
print("Chicken - Php.100")
print()

#Get order
validItems = ["hamburger", "chicken"]
while True:
    food = input("Enter a food to buy ('done' to quit): ")
    if food.lower() == 'done':
        break
    elif food.lower() not in validItems:
        print("Invalid menu item. Please choose from the following:")
        for item in validItems:
            print(f"- {item.capitalize()}")
    else:
        quantity = int(input("Quantity: "))
        price = float(input(f"Enter the price of a {food}: Php."))
        
        foods.append(food)
        quantities.append(quantity)
        prices.append(price * quantity)

#Cart display
print("________________________")
print("YOUR CART:")
for i in range(len(foods)):
    print(f"{quantities[i]} x {foods[i]} - Php.{prices[i]}")
print("------------------------")

for price in prices:
    total += price
print(f"Your total is: Php.{total}")
print("------------------------")

#Payment
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