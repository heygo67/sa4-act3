number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? (enter \"q\" to quit.) "))

while guess != "q":
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input(f"Sorry! Try again! (enter \"q\" to quit.) ")
        if guess == "q":
            print(f'The correct number was {number}. Thanks for playing!')
            break


