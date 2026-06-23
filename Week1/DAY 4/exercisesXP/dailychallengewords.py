
#Key Python Topics:
#input() function
##Strings and string manipulation
#Loops (for or while)
##Conditional statements (if)
#Instructions:
#1. Ask the user for a string.
#2. Write a program that processes the string to remove consecutive duplicate letters.
#The new string should only contain unique consecutive letters.
#For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
#3. The program should print the modified string.







word = input("Enter a word: ")

new_word = ""

for letter in word:
    if new_word == "" or letter != new_word[-1]:
        new_word = new_word + letter

print(new_word)