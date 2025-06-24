#Shopping Cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter food item or press e to exit ")
    if food.lower() == 'e':
        break
    else : 
        price = float(input(f"Enter price for {food}:R "))
        foods.append(food)
        prices.append(price)
        
print("\Shopping Cart:")

for foods in foods:
    print(foods, end=' ')
    
for price in prices:
    total += price
    
print("\n")
print(f"Total: R {total:.2f}") # the f function formats the string. This is used to format the total price to 2 decimal places.
print("Thank you for shopping with us!")    
    
       