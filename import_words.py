from random import choice

def word_store(file_name: str): # vardu lasišāna un izvele
    words = []
    file = open(file_name, "r")
    for word in file:
        words.append(word[:-1])
    rword = choice(words)
    return rword