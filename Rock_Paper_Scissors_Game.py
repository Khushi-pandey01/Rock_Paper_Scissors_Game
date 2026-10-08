import random

def main():
    while True:
        print("\n" + "=" * 50)
        print("🎮 WELCOME TO ROCK PAPER SCISSORS GAME 🎮".center(50))
        print("=" * 50)

        user_score = 0
        comp_score = 0

        round_no = 0
        tie_count = 0
        max_rounds = 3

        while round_no < max_rounds:
            user = get_user()
            comp = get_computer()

            print(f"\n You chose: {show(user)}")
            print(f" Computer chose: {show(comp)}")

            result = check_winner(user, comp)

            if result == "tie":
                tie_count += 1

                if tie_count == 2:
                    print("\n🔁 Too many ties! Restarting game...\n")
                    user_score = 0
                    comp_score = 0
                    round_no = 0
                    tie_count = 0

                continue

            tie_count = 0
            round_no += 1

            if result == "win":
                user_score += 1
            else:
                comp_score += 1

        print("\n" + "=" * 50)
        print("📊 FINAL SCORE".center(50))
        print("=" * 50)

        print(f"👤 User     : {user_score}")
        print(f"💻 Computer : {comp_score}")

        print("-" * 50)

        if user_score > comp_score:
            print(" RESULT   : YOU WIN! 🏆")
        elif comp_score > user_score:
            print(" RESULT   : COMPUTER WINS! 🎉")
        else:
            print(" RESULT   : DRAW! 🤝")

        print("=" * 50)

        while True:
            choice = input("\n Do you want to play again? (y/n): ").lower().strip()

            if choice == "y":
                break   # restart full game loop

            elif choice == "n":
                print("\n" + "=" * 50)
                print("😃 THANKS FOR PLAYING! SEE YOU NEXT TIME 👋".center(50))
                print("=" * 50)
                return   # exit program

            else:
                print("❌ Please enter only 'y' or 'n'!")


def get_user():
    while True:
        print("\n" + "-" * 50)
        choice = input("👉 Enter rock / paper / scissors: ").lower().strip()

        if choice in ["rock", "paper", "scissors"]:
            return choice

        print("❌ Invalid input!")


def get_computer():
    return random.choice(["rock", "paper", "scissors"])


def show(choice):
    return {
        "rock": "Rock ✊",
        "paper": "Paper 📄",
        "scissors": "Scissors ✂️"
    }[choice]


def check_winner(u, c):
    if u == c:
        print("\n🤝 It's a TIE! Replaying round...")
        return "tie"

    if (u == "rock" and c == "scissors") or \
       (u == "paper" and c == "rock") or \
       (u == "scissors" and c == "paper"):
        print("\n🏆 YOU WIN THIS ROUND!")
        return "win"

    print("\n💻 COMPUTER WINS THIS ROUND!")
    return "lose"

if __name__ == "__main__":
    main()