# Recap: What is a float? What’s the difference between a float and an integer? Create a list containing the following sequence of mixed types: floats and integers: 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#  Avoid hard-coding each number manually. Think: Can you generate this sequence using a loop or another method?

numbers = []

for i in range(3, 11):
    numbers.append(i / 2)

print(numbers)