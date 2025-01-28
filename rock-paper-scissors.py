import random

# Print game rules
print(
    "Winning rules of the game ROCK PAPER SCISSORS are:\n"
    "Rock vs Paper -> Paper wins\n"
    "Rock vs Scissors -> Rock wins\n"
    "Paper vs Scissors -> Scissors wins\n"
)

def get_choice_name(choice):
    """Convert numerical choice to its corresponding name."""
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Scissors"
    elif choice == 3:
        return "Paper"
    return "Invalid"

def decide_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (
        (user_choice == 1 and computer_choice == 2) or  # Rock beats Scissors
        (user_choice == 2 and computer_choice == 3) or  # Scissors beats Paper
        (user_choice == 3 and computer_choice == 1)     # Paper beats Rock
    ):
        return "Congratulations! You won!"
    else:
        return "You lose! Computer wins."

def play_again():
    """Ask the player if they want to play again."""
    while True:
        replay = input('Do you want to play again? (Y/N): ').lower()
        if replay == 'y':
            return True
        elif replay == 'n':
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# Game loop
game_on = True
while game_on:
    # Generate computer's choice for each round
    computer_choice = random.randint(1, 3)

    # Prompt user for their choice
    try:
        user_choice = int(input('Choose your number: 1 - "Rock", 2 - "Scissors", 3 - "Paper": '))
        if user_choice not in [1, 2, 3]:
            print("Invalid choice! Please select a number between 1 and 3.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Display choices
    print(f"\nYou chose {get_choice_name(user_choice)}")
    print(f"The computer chose {get_choice_name(computer_choice)}")

    # Determine and display the result
    result = decide_winner(user_choice, computer_choice)
    print(result)

    # Ask if the user wants to play again
    game_on = play_again()

print("Thank you for playing! Goodbye!")
