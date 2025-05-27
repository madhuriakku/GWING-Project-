import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return 'draw'
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return 'user'
    else:
        return 'computer'

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.\n")

    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        user_choice = input("👉 Your choice (rock/paper/scissors): ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("❗ Invalid input. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🖥️ Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)

        if result == 'user':
            print("✅ You win this round!")
            user_wins += 1
        elif result == 'computer':
            print("❌ Computer wins this round!")
            computer_wins += 1
        else:
            print("⚖️ It's a draw!")
            draws += 1

        print(f"📊 Score: You {user_wins} | Computer {computer_wins} | Draws {draws}\n")

    print("🏁 Final Score:")
    print(f"You: {user_wins}")
    print(f"Computer: {computer_wins}")
    print(f"Draws: {draws}")

    if user_wins > computer_wins:
        print("🎉 You are the overall winner!")
    elif computer_wins > user_wins:
        print("💻 Computer wins overall!")
    else:
        print("⚖️ It's an overall draw!")

# Run the game
play_game()
