# name = 

# word = input("Please enter a word: ")

# new_word = list(word)
# new_word.reverse()
# new_word = "".join(new_word)

# print((new_word))

# while 10 > 1:
#     word = input("Please enter a word: ")     
#     new_word = list(word) 
#     new_word.reverse()
#     new_word = "".join(new_word)
# print(new_word)
while True:
    word = input("Please enter a word: ")
    new_word = list(word)
    new_word.reverse()
    new_word = "".join(new_word)

    if word == new_word:
        print("This word", word,"is a palindrome")
    else:
        print("This word", word, "is not a palindrome")

    
