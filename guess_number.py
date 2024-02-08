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
            guess = input(f"Sorry! Try again! {guesses} guess(es) left! (enter \"q\" to quit.) ")
            if guess == "q":
                print(f'The correct number was {number}. Thanks for playing!')
                break


