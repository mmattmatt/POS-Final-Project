foods = []
prices = []
total = 0

while True:
    print("\nMenu:")
    print ()
    food = input("Enter a food to buy ('done' to quit): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price of a {food}: Php."))
        foods.append(food)
        prices.append(price)
print()
print("______________________")
print()
print("YOUR CART:")
for food in foods:
    print(food)
print("______________________")

for price in prices:
    total += price
print()
print(f"Your total is: Php.{total}")
print("______________________")