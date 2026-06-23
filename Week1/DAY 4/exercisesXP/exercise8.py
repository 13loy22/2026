##🌟 Exercise 8: Pizza Toppings
#Key Python Topics:

#Loops
#Lists
#String formatting
#Instructions:Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.For each topping entered, print:
"Adding [topping] to your pizza." 
#After exiting the loop, print all the toppings and the total cost of the pizza.
#he base price is $10, and each topping adds $2.50.

# Exercise 8: Pizza Toppings

toppings = []
price = 10

while True:
    topping = input("Enter a topping (or type 'quit'): ")

    if topping == "quit":
        break

    toppings.append(topping)
    price = price + 2.5

    print("Adding", topping, "to your pizza.")

print("Toppings:", toppings)
print("Total cost: $", price)


