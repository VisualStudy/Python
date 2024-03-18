pizza_toppings = ["cheese", "pepperoni", "banana"]

print("We have the following toppings:")

for topping in pizza_toppings:
    if topping == "cheese":
        print(f"{topping} (free)")
    else:
        print(f"{topping} ($1.00)")
