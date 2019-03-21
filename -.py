 #THIS IS GIVEN ME ERROR????
# document =  open("research.txt" , "r")
# for line in document.readlines():
#     print(line)


document_list = []
document =  open(r"C:\Users\ogidan tosin\Desktop\PYTHON TRAINING\MY CODES\research.txt")




# def add_to_score():
   

for line in document.readlines():
    document_list = (line.split())    

def request_to_play():
    request_to_play_a_game = input("Do you want to play a game?")
    if request_to_play_a_game == "yes":

        play_a_game()

# def request_to_keep_play():
#     request_to_play_a_game = input("Do you still want to play?")
#     if request_to_play_a_game == "yes":        
#         play_a_game()


def play_a_game():
    score = 0 
    while True:                  
        guessed_word = input("Guess a word?")
        if guessed_word in document_list:
            score += 2
            print("you guessed right and earn 2 points")
            print("your total score is ",score)           
        elif guessed_word not in document_list:
            score -= 1
            print("sorry, wrong guess. you just lost 1 point")
            print("your total score is ",score)    
       
request_to_play()            
