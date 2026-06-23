

# Exercise 6: While Loop  🌟 Exercise 6: While Loop 
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop


while True:
    name = input("Enter your name: ")

    if not name.isdigit() and len(name) >= 3:
        print("thank you")
        break
    else:
        print("give the correct name:")