numbers = [1, 2, 3]
print(numbers)
print(numbers[0])

pizza_toppings = ["cheese", "pepperoni"]

print(pizza_toppings)
print(len(pizza_toppings))

pizza_toppings.append("pineappple")
print(pizza_toppings)

pizza_toppings.insert(0, "banana")
print(pizza_toppings)

del pizza_toppings[1]
print(pizza_toppings)

pizza_toppings.pop()
print(pizza_toppings)

pizza_toppings.remove("banana")
print(pizza_toppings)

mixed_list = [1, "chesse", 2, "pepperoni"]
print(mixed_list)

list_of_lists = [[1, 2], [2, 3]]
print(list_of_lists[0])
print(list_of_lists[1][1]) # 3
