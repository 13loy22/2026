#Instructions:
#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
##Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.


my_fav_numbers = {4, 8, 11}

my_fav_numbers.add(15)
my_fav_numbers.add(20)

my_fav_numbers.remove(20)

friend_fav_numbers = {5, 8, 12}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(my_fav_numbers)
print(friend_fav_numbers)
print(our_fav_numbers)