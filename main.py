#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def number_guessing_name():
    # dependencies
    import random
    import os
    
    def clear():
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
    
    from art import logo
    
    print(logo)
    
    # variables for thumbs up and down
    thumbs_up = "\U0001F44D"
    thumbs_down = "\U0001F44E"
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # getting a random number from the raffle drum
    raffle_drum = list(range(1, 101))
    lucky_number = random.choice(raffle_drum)
    
    # uncomment the following line of code if you want to know the answer beforhand
    # print(f"Psssst, the correct answer is {lucky_number}")
    
    # asking user for difficulty and stating the 3 different possible outcomes
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == "easy":
        chances = 10
    elif difficulty == "hard":
        chances = 5
    else:
        print("Invalid difficulty level. Defaulting to 'easy'.")
        chances = 10
    
    # depending on the users answer, this lines will give more or less attempts to user
    print(f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    # giving the user clues on whether they are close to the lucky number and reminding them of their turns left
    while chances > 0 and guess != lucky_number:
        if guess == lucky_number:   # if they get it right this will be printed
            print(f"You got it, the answer was {lucky_number}")
            break                   # and the loop will stop
        elif guess > lucky_number:
            print(f"Too high {thumbs_up}")  # if the number they guessed is above, this will be printed
        elif guess < lucky_number:
            print(f"Too low {thumbs_down}")  # if the number they guessed is below, this will be printed
    
        # everytime they make a mistake the number of chances will be reduced by one
        # and it will keep reminding them their chances left as well as asking them for another number
        chances -= 1   
        if chances > 0:
            print(f"You have {chances} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
        else:
            print("You've run out of guesses, you lose.")  # if they dont manage to do it, the lose
    
    # just a final reminder wether they won or lost to clarify their final result and the lucky number 
    if guess == lucky_number:
        print(f"You got it, the answer was {lucky_number}")
    else:
        print(f"The lucky number was: {lucky_number}")

    # asking user if they are up for another round if "yes" it will clear and start again if "no" it will just clear
    play_again = input("do you want to play again 'y' or 'n': ")
    if play_again == "y":
        clear()
        number_guessing_name()
    else:
        clear()

number_guessing_name()


