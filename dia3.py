def vocals_counter(word):
    counter = 0
    word = word.lower()
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": 
            counter += 1

    return counter

user_word = input("Escribe una palabra: ")
vocals = vocals_counter(user_word)
print(f"{user_word} tiene {vocals} vocales ")