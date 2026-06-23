#Exercise 9: Cinemax Tickets
#Key Python Topics:

#Conditionals
#Lists
#Loops


#Instructions:

#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.


total_cost = 0

while True:
    age = input("Enter age (or type 'done'): ")

    if age == "done":
        break

    age = int(age)

    if age < 3:
        total_cost = total_cost + 0
    elif age <= 12:
        total_cost = total_cost + 10
    else:
        total_cost = total_cost + 15

print("Total cost:", total_cost)