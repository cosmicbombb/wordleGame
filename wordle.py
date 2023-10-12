import random


#word to be guessed
hidden_word = random.choice(["this", "five", "lake", "yolo", "wack", "pink"])

#number of attempts the user is allowed
attempt = 5


def give_instructions():
    print('''\n Wordle is a word guessing game.
    You have 5 attempts
    (*) means the letter was in the word in the correct position
    ($) means the letter is in the word but not in the correct position 
    (x) means the letter is not in the word
        
    Best of luck!''')
    

def check_word(guess):
    #the word guessed was correct
    if hidden_word == guess:
        print("Congrats!! You did it.")
        return True
    result = ""
    #zip pairs
    for i,j in zip(guess, hidden_word):
        if i == j:
            #the letter is correct
            result += ("*")    
        elif i in hidden_word:
            #the letter is in the word but not the correct spot
            result += ("$")    
        else:
            #the letter is not in the word
            result += ("x") 
    print(result)
    return False


def main():
    attempt = 5
    give_instructions()
    while attempt > 0:
        guess = input("Enter a four letter word: ")
        if check_word(guess):
            break
        else:
            #attempt = attempt - 1
            attempt -= 1
            print(f"You have {attempt} attempts left.")
    else:
        print("GAME OVER! :(")


if __name__ == "__main__":
    main()
