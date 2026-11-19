from game_setup import choose_difficulty
from input_handler import get_guess
from guess_checker import check_guess
from results import display_result, play_again


def play_game():

    print("\n===== NUMBER GUESSING GAME =====")

    secret_number, max_attempts = choose_difficulty()

    won = False
    attempts_used = 0

    for attempt in range(1, max_attempts + 1):

        guess = get_guess(attempt)
        attempts_used = attempt

        result = check_guess(guess, secret_number)

        if result == "correct":
            won = True
            break

        elif result == "high":
            print("Too high! Try again.")

        else:
            print("Too low! Try again.")

    display_result(won, attempts_used, secret_number)


if __name__ == "__main__":

    while True:

        play_game()

        if not play_again():
            print("\nThanks for playing!")
            break