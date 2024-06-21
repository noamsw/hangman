# import nltk
import random
# import Counter
# nltk.download('words')

words_list = ['apple', 'house', 'dog', 'book', 'car', 'tree', 'cat', 'sun', 'bird', 'child', 
 'day', 'eye', 'family', 'food', 'friend', 'game', 'hand', 'home', 'life', 'man', 
 'money', 'mother', 'night', 'party', 'person', 'place', 'school', 'story', 'time', 
 'water', 'woman', 'world', 'animal', 'beach', 'bed', 'boat', 'camera', 'city', 
 'computer', 'country', 'dance', 'dream', 'earth', 'flower', 'girl', 'hair', 
 'happiness', 'hat', 'holiday', 'horse', 'job', 'journey', 'lake', 'love', 
 'mountain', 'music', 'ocean', 'paint', 'pen', 'pencil', 'picture', 'rain', 
 'river', 'road', 'sea', 'sky', 'star', 'street', 'table', 'train', 'tree', 
 'vacation', 'valley', 'village', 'voice', 'war', 'water', 'way', 'wind', 
 'window', 'year', 'youth', 'adventure', 'afternoon', 'baby', 'ball', 'bell', 
 'bird', 'bridge', 'building', 'bush', 'butterfly', 'cake', 'candle', 'candy', 
 'castle', 'cloud', 'crown', 'diamond', 'dress', 'egg', 'feather', 'fire']



def printMan(num):
    if num == 0:
        print("-----")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 1:
        print("-----")
        print("|   |")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 2:
        print("-----")
        print("|   |")
        print("|   0")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 3:
        print("-----")
        print("|   |")
        print("|   0")
        print("|   |")
        print("|    ")
        print("|    ")
        print("|_   ")
    if num == 4:
        print("-----")
        print("|   |")
        print("|   0")
        print("|   |\\")
        print("|    ")
        print("|    ")
        print("|_    ")
    if num == 5:
        print("-----")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|    ")
        print("|    ")
        print("|_    ")
    if num == 6:
        print("-----")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|    \\")
        print("|    ")
        print("|_    ")
    if num == 7:
        print("-----")
        print("|   |")
        print("|   0")
        print("|  /|\\")
        print("|  / \\")
        print("|    ")
        print("|_    ")

def printWord(arr):
    print(''.join(arr))

if __name__ == "__main__":
    random_word = random.sample(words_list, 1)[0]
    letters_inword = {}
    for i in range(len(random_word)):
        if random_word[i] in letters_inword:
            letters_inword[random_word[i]].append(i)
        else:
            letters_inword[random_word[i]] = [i]
    letters_guessed = set()
    num_guesses = 7
    incorrect_guesses = 0
    n = len(random_word)
    current_word = ["_",' '] * n
    currentlen = 0

    # print(random_word)
    print("Hello, welcome to hangman, you have 7 guesses to get the word right")
    print(f'your word has {n} letters in it')
    printWord(current_word)
    user_input   = input("please enter your first guess: ").lower()
    while True:
        if len(user_input) != 1:
            while True:
                print("only enter a single letter please")
                user_input = input("enter a valid guess: ").lower()
                if len(user_input) == 1:
                    print("awesome!")
                    break
        if not user_input.isalpha():
            while True:
                print("only enter a letter please")
                user_input = input("enter a valid guess: ").lower()
                if user_input.isalpha():
                    print("awesome!")
                    break
        if user_input in letters_guessed:
            while True:
                print("you already guessed that letter")
                user_input = input("enter a new letter: ").lower()
                if user_input not in letters_guessed:
                    print("awesome!")
                    break
        if user_input in letters_inword:
            print("awesome! you guessed a correct letter!!")
            for place in letters_inword[user_input]:
                current_word[2*place] = user_input
                currentlen+=1
            if currentlen == n:

                print("awesome! you Won!")
                quit()
            
        else:
            print("sorry, you got it wrong")
            incorrect_guesses+=1
            print(f"you have made {incorrect_guesses} incorrect guesses")
            print(f"you have {num_guesses - incorrect_guesses} guesses left")
            if num_guesses == incorrect_guesses:
                print("you lost :(")
                quit()
        letters_guessed.add(user_input)
        printMan(incorrect_guesses)
        printWord(current_word)
        user_input = input("please enter your next guess: ").lower()
        
