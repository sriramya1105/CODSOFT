import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to decide the winner
def decide_winner(user_choice, computer_choice):
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if user_choice == computer_choice:
        return "tie"
    elif winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

# Function to display results
def display_result(user_choice, computer_choice, result, user_score, computer_score):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    print(f"Score -> You: {user_score}, Computer: {computer_score}\n")

# Function to play a single round
def play_round(user_score, computer_score):
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == 'exit':
        return False, user_score, computer_score
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return True, user_score, computer_score

    computer_choice = get_computer_choice()
    result = decide_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1

    display_result(user_choice, computer_choice, result, user_score, computer_score)
    return True, user_score, computer_score

# Main function to handle the game loop
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'exit' at any time to quit the game.\n")

    while True:
        continue_game, user_score, computer_score = play_round(user_score, computer_score)
        if not continue_game:
            break

    print("Final Scores:")
    print(f"You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")

# Start the game
main()