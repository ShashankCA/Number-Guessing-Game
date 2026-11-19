import random

def choose_difficulty():

    print("\nSelect Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter choice: ")

    if choice == "1":
        return random.randint(1, 50), 10

    elif choice == "2":
        return random.randint(1, 100), 7

    elif choice == "3":
        return random.randint(1, 200), 5

    else:
        print("Invalid choice! Selecting Medium.")
        return random.randint(1, 100), 7