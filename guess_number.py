number = 10
guesses = 5

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? (enter \"q\" to quit.) "))


while guesses != 0:
    while guess != "q":
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        else:
            guesses += -1
            if guesses == 0:
                print(f'Ran out of guesses! The correct number was {number}')
                break
            if guess > number:
                guess = input(f"Sorry, too high! {guesses} guesses left. Try again! (enter \"q\" to quit.) ")
                if guess == "q":
                    print(f'The correct number was {number}. Thanks for playing!')
                    break
                else:
                    guess = int(guess)
            elif guess < number:
                guess = input(f"Sorry, too low! {guesses} guesses left. Try again! (enter \"q\" to quit.) ")
                if guess == "q":
                    print(f'The correct number was {number}. Thanks for playing!')
                    break
                else:
                    guess = int(guess)
            if guess == "q":
                print(f'The correct number was {number}. Thanks for playing!')
                break



