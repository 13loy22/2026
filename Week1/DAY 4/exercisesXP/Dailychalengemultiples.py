#Challenge 1: Multiples of a Number
#Key Python Topics:
#input() function
##Loops (for or while)
#Lists and appending items
#Basic arithmetic (multiplication)
#Instructions:
#1. Ask the user for two inputs:
#A number (integer).
#A length (integer).
#2. Create a program that generates a list of multiples of the given number.
#3. The list should stop when it reaches the length specified by the user.

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)