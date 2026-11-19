def check_guess(guess, secret_number):

    if guess == secret_number:
        return "correct"

    elif guess > secret_number:
        return "high"

    else:
        return "low"