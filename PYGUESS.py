import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    # Difficulty selection
    choice = input("Enter your choice: ")
    if choice == "1":
        attempts = 10
        print("Great! You have selected the Easy difficulty level.")
    elif choice == "2":
        attempts = 5
        print("Great! You have selected the Medium difficulty level.")
    elif choice == "3":
        attempts = 3
        print("Great! You have selected the Hard difficulty level.")
    else:
        print("Invalid choice! Defaulting to Medium (5 chances).")
        attempts = 5

    print("Let's start the game!")

    # Random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts_used = 0

    while attempts_used < attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts_used += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number in {attempts_used} attempts.")
            break
        elif guess > number_to_guess:
            print(f"Incorrect! The number is less than {guess}.")
        else:
            print(f"Incorrect! The number is greater than {guess}.")

    else:  # If loop completes without break
        print(f"Sorry! You've used all your {attempts} attempts. The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()