
def get_guess(attempt):
    while True:
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

            if guess > 0:
                return guess
            else:
                print("Enter a positive number.")

        except ValueError:
            print("Invalid input! Enter a number.")
