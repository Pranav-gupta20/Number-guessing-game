from random import randint

Easy_level_turns = 10
Hard_level_turns = 5



def check_answer(user_guess,actual_guess,turn):
    '''function to check userguess against actualguess'''
    if user_guess > actual_guess:
        print("Too High")
        return turn-1
    elif user_guess < actual_guess:
         print("Too Low")
         return turn-1
    else:
        print(f"You get it! your answer is {actual_guess}.")


def set_difficulty():
    '''Fucntion to set difficulties'''
    level=input("Choose your difficulty. type 'easy' or 'hard'\n ")
    if level=='easy':
        return Easy_level_turns        
    else:
        return Hard_level_turns


def game():
    '''repeating the guessing fucntionality if get it wrong'''
    print("welcome to NumBer Guessing Game. ")    
    print("I'm Thinking about a Number betwwen '0' and '100' ")
    answer= randint(1 , 100)
    turns = set_difficulty()
     
    guess=0 
    while guess != answer:
        print(f"your have {turns} turns left, Guess again")
        guess=int(input("make a guess: "))
        turns = check_answer(guess, answer , turns)
        if turns ==0:
            print(f"you have run out of guess, You Loose. The anser was {answer}")
            return
        elif guess != answer:
            print("guess again")

game()            