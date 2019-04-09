import string
import random

f = open("twist.txt","r")
case = f.readline()
# f.closed()
words = str.split(case, " ")

# print(words)
def len_words():
    len_words = int(0)
    if len(words) >= 2:
        len_words += 1
        return len_words

len_words()

def levels():
    levels = 1
    for elements in words:
        if len(words) >= 2:
            levels += 1
            return levels

levels()    

def pick_a_word(word):
    word = random.choice(words)
    print(f"---->Testing, the word is {word}<----")
    return word    
    # print(word)

pick_a_word(words)

def enter_guess():
    guess_word = input("Guess a word: ")
    if guess_word == words:
        return guess_word
    else:
        print("Come on, you have to guess a word")
        enter_guess    

def assess_guess(word, tries, score):
    10 > 1 == True
    while True:
        score = 0
        guess_word = enter_guess()
        if guess_word == word:
            tries -= 0
            score += 10
            print(f"Einstein!, your score is {score}, way to go")
        if guess_word != word:
            tries -= 1
            score -= 5
            print(f"Wrong, you have {tries} tries left, and your score is {score}")
            assess_guess(word, tries, score)
        break
    else:
        print("Sorry, you've exhausted your tries.")
        return False
    return True


### Playing game
def Gameplay(count):
    count = 1
    word = pick_a_word(words)
    level = levels()
    print                      ("    /````````````````````\ ")
    print                      ("   /       WELCOME        \ ")
    print                      ("  /          TO            \ ")
    print                      (" /________THE WORD__________\ ")
    print                      ("/_______GUESSING GAME________\ ")

    while assess_guess(word, 10, 0):
        ask = input("Do you want to continue?: ")
        if  ask == "y" or "yes":
            count += 1
            Gameplay(count)		
        else:		
            print("You played", count, "game")
            print("0_0 Goodbye 0_0")
            exit
    else:
        print("Oops you missed that one")
        retry =input("Do you want to try another word?")
        if  retry == "y" or "yes":
            Gameplay(count)
        else:
            print("0_0 Goodbye 0_0")
			
Gameplay(0)

def start():
    for i in words:
        if words == len(words) >= 2:
            words += 1
            return words
start()