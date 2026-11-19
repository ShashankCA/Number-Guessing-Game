# Number Guessing Game

A modular command-line Number Guessing Game built in Python as part of a collaborative Git workflow assignment.

## Features

- **Difficulty Selection & Setup:** Generates random target numbers based on the selected difficulty level (`game_setup.py`).
- **Input Validation:** Ensures user guesses are valid integers within the expected range (`input_handler.py`).
- **Guess Evaluation:** Compares user guesses against the target number and provides feedback (`guess_checker.py`).
- **Result Tracking & Replay:** Displays final game outcomes and allows players to start a new round (`results.py`).

## Project Structure

```text
Number-Guessing-Game/
├── game_setup.py      # Random number generation and difficulty selection
├── input_handler.py   # User input handling and validation
├── guess_checker.py   # Logic for checking guesses against the target
├── results.py         # End-of-game summary and replay functionality
├── main.py            # Main entry point integrating all game modules
└── README.md          # Project documentation
