# import nltk
import random
# nltk.download('words')

# word_list = words.words()

# random_word = random.sample(word_list, 1)

num_guesses = 12

guesses = 0

def printMan(num):
    if num == 0:
        print("-----")
        print("|   |")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 1:
        print("-----")
        print("|   |")
        print("|   0")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 2:
        print("-----")
        print("|   |")
        print("|   0")
        print("|   |")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 3:
        print("-----")
        print("|   |")
        print("|   0")
        print("|   |\\")
        print("|    ")
        print("|    ")
        print("|_    ")
    if num == 4:
        print("-----")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|    ")
        print("|    ")
        print("|_    ")
    if num == 5:
        print("-----")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|    \\")
        print("|    ")
        print("|_    ")
    if num == 6:
        print("-----")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|  / \\")
        print("|    ")
        print("|_    ")
    