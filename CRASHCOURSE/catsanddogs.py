human_years = int(input("Enter human years: "))

# Calculate cat years
if human_years == 1:
    cat_years = 15
elif human_years == 2:
    cat_years = 15 + 9
else:
    cat_years = 15 + 9 + (human_years - 2) * 4

# Calculate dog years
if human_years == 1:
    dog_years = 15
elif human_years == 2:
    dog_years = 15 + 9
else:
    dog_years = 15 + 9 + (human_years - 2) * 5

# Output
print([human_years, cat_years, dog_years])
