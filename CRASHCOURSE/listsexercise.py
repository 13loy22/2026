

# 1.Given a list [1, 2, 3, 4], print out all the values in the list one by one.



numbers = [1, 2, 3, 4]

print("Exercise 1")

for number in numbers:
    print(number)


# 2. Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.



print("\nExercise 2")

for number in numbers:
    print(number * 20)


# 3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].



print("\nExercise 3")

names = ["Elie", "Tim", "Matt"]

new_list = []

for name in names:
    new_list.append(name[0])

print(new_list)


# 4. Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].



print("\nExercise 4")

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# 5. Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].



print("\nExercise 5")

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for number in list1:
    if number in list2:
        common.append(number)

print(common)


# 6.Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].



print("\nExercise 6")

words = ["Elie", "Tim", "Matt"]

new_list = []

for word in words:
    new_list.append(word.lower()[::-1])

print(new_list)


# 7. Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].



print("\nExercise 7")

string1 = "first"
string2 = "third"

letters = []

for letter in string1:
    if letter in string2 and letter not in letters:
        letters.append(letter)

print(letters)


# 8.For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].



print("\nExercise 8")

numbers = []

for number in range(1, 101):
    if number % 12 == 0:
        numbers.append(number)

print(numbers)


# 9.Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].



print("\nExercise 9")

word = "amazing"

letters = []

for letter in word:
    if letter not in "aeiou":
        letters.append(letter)

print(letters)


# 10. Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].



print("\nExercise 10")

result = []

for i in range(3):
    result.append([0, 1, 2])

print(result)


# 11. Generate a list with the following structure
#[
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#]




print("\nExercise 11")

result = []

for i in range(10):
    result.append([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(result)