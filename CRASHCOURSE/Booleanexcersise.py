# 1. Declare a variable called first and assign it to the value "Hello World"
first = "Hello World"

# 2. Write a comment that says "This is a comment."
# This is a comment.

# 3. Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# 4. If statement that checks if 1 is less than 2 and if 4 is greater than 2
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# 5. Assign a variable called nope to an absence of value
nope = None

# 6. Use "and" to combine True with False
True and False  # Result: False

# 7. Calculate the length of the string "What's my length?"
len("What's my length?")  # Result: 17

# 8. Convert the string "i am shouting" to uppercase
"i am shouting".upper()  # Result: "I AM SHOUTING"

# 9. Convert the string "1000" to the number 1000
int("1000")  # Result: 1000

# 10. Combine the number 4 with the string "real" to produce "4real"
str(4) + "real"  # Result: "4real"

# 11. Record the output of the expression 3 * "cool"
3 * "cool"  # Result: "coolcoolcool"

# 12. Record the output of the expression 1 / 0
1 / 0  # Result: ZeroDivisionError: division by zero

# 13. Determine the type of []
type([])  # Result: <class 'list'>

# 14. Ask the user for their name, store it in a variable called name
name = input("What is your name? ")

# 15. Ask the user for a number and check if negative, positive, or zero
number = int(input("Enter a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# 16. Find the index of "l" in "apple"
"apple".index("l")  # Result: 3

# 17. Check whether "y" is in "xylophone"
"y" in "xylophone"  # Result: True

# 18. Check whether a string called my_string is all in lowercase
my_string = "example"
my_string.islower()  # Result: True
