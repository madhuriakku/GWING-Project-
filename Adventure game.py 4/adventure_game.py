story = {
    "start": {
        "text": "Hello {player}, you are in a dark forest...",
        "choices": {
            "left": "river",
            "right": "cave"
        }
    },
    "river": {
        "text": "You arrive at a river. You can swim or walk.",
        "choices": {
            "swim": "shark",
            "walk": "village"
        }
    },
    "cave": {
        "text": "You enter a cave and see a sleeping bear. Sneak or run?",
        "choices": {
            "sneak": "treasure",
            "run": "start"
        }
    },
    "shark": {
        "text": "A shark eats you. Game over.",
        "choices": {}
    },
    "village": {
        "text": "You find a village and live happily. You win!",
        "choices": {}
    },
    "treasure": {
        "text": "You find treasure. You win!",
        "choices": {}
    }
}

def play_game():
    current_scene = "start"

    while True:
        scene = story[current_scene]
        print("\n" + scene["text"])

        if not scene["choices"]:
            print("The End.")
            break

        print("Choices:", ", ".join(scene["choices"].keys()))
        choice = input("What do you choose? ").lower()

        if choice in scene["choices"]:
            current_scene = scene["choices"][choice]
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    play_game()
