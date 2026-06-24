# . Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).


 
pairs = [("name", "Elie"), ("job", "Instructor")]

my_dict = {}

for item in pairs:
    my_dict[item[0]] = item[1]

print(my_dict)


#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.



states = ["CA", "NJ", "RI"]
names = ["California", "New Jersey", "Rhode Island"]

my_dict = {}

for i in range(len(states)):
    my_dict[states[i]] = names[i]

print(my_dict)


# Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should 
# look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

vowels = ["a", "e", "i", "o", "u"]

my_dict = {}

for vowel in vowels:
    my_dict[vowel] = 0

print(my_dict)


# 4 Create a dictionary where the key is the position of the 
# letter in the alphabet, and the value is the letter itself. You should return something like this:

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

my_dict = {}

for i in range(len(letters)):
    my_dict[i + 1] = letters[i]

print(my_dict)


# SUPER BONUS

word = "awesome sauce"

my_dict = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

for letter in word:
    if letter in my_dict:
        my_dict[letter] = my_dict[letter] + 1

print(my_dict)