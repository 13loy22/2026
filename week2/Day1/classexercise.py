people = ('rick', 'morty', 'beth', 'jerry', 'snowball')

short_names = filter(lambda name: len(name) <= 4, people)

greetings = map(lambda name: "Hello " + name, short_names)

for greeting in greetings:
    print(greeting)

    # annother option
    #people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# Using map and filter, try to say hello to everyone whose name is less than or equal to 4 letters

#def say_hello(name):
 #
#def check_length(name):
 #   return len(name) <= 4

filtered_names = list(filter(check_length, people))

hi = list(map(say_hello, filtered_names))

print(hi)