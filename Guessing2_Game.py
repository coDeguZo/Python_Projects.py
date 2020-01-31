# Guessing Game Project

#Variables
secret_word = "Shrek"
guess = ""
guess_count = 0
guess_limit = 5
no_more_guesses = False
wrong_guess = "Good Guesss!!! :)"

print("This an Animated Charater that is green!")
while guess != secret_word and not(no_more_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess here: ")
        guess_count += 1
        if guess != secret_word:
            print('Try Again')
        else:
            print(wrong_guess)
    else:
        no_more_guesses = True

if no_more_guesses:
    print("Better Luck Next Time Buddy")
else:
    print("Good Job!")


    