
def display_result(won, attempts, secret_number):

    if won:
        print("\nCongratulations! You guessed correctly.")
        print("Attempts used:", attempts)

    else:
        print("\nGame Over!")
        print("The correct number was:", secret_number)


def play_again():

    choice = input("\nDo you want to play again? (y/n): ")

    return choice.lower() == "y"
