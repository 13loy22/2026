#Bonus:Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.


attendees = []

while True:
    age = input("Enter age (or type 'done'): ")

    if age == "done":
        break

    age = int(age)

    if age >= 16 and age <= 21:
        attendees.append(age)

print("Final attendees:", attendees)