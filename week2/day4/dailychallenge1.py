def sort_words():
    user_words = input("Enter words separated by commas: ")

    words_list = user_words.split(",")

    words_list.sort()

    sorted_words = ",".join(words_list)

    print(sorted_words)


sort_words()