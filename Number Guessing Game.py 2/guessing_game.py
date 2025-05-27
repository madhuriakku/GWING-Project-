import random

def choose_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")

    while True:
        try:
            lower = int(input("\nEnter the lower bound of the range: "))
            upper = int(input("Enter the upper bound of the range: "))
            if lower >= upper:
                print("⚠️ Invalid range! Lower must be less than upper.")
                continue
        except ValueError:
            print("❗ Please enter valid integers.")
            continue

        secret_number = random.randint(lower, upper)
        max_attempts = choose_difficulty()
        attempts = 0

        print(f"\n🔢 I have selected a number between {lower} and {upper}.")
        print(f"💡 You have {max_attempts} attempts to guess it!")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < secret_number:
                    print("🔻 Too low!")
                elif guess > secret_number:
                    print("🔺 Too high!")
                else:
                    print(f"✅ Correct! You guessed it in {attempts} attempt(s).")
                    break
            except ValueError:
                print("❗ Please enter a valid number.")

        else:
            print(f"❌ You've used all {max_attempts} attempts. The number was {secret_number}.")

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("👋 Thanks for playing! Goodbye!")
            break

# Run the game
number_guessing_game()
