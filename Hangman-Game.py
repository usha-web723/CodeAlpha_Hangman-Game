import random

# Dictionary of words and hints
word_list = {
    "rocket": "Used to travel into space",
    "guitar": "A musical instrument",
    "camera": "Used to take photos",
    "library": "A place where books are kept",
    "planet": "Earth is one of these"
}

print("===================================")
print("      🎮 WELCOME TO HANGMAN 🎮")
print(" Guess the word one letter at a time")
print(" You have only 6 wrong chances!")
print("===================================\n")

while True:

    # Select a random word
    secret_word = random.choice(list(word_list.keys()))
    hint = word_list[secret_word]

    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []
    chances = 6

    print("\n💡 Hint:", hint)

    # Game Loop
    while chances > 0 and "_" in guessed_word:

        print("\nWord:", " ".join(guessed_word))
        print("Guessed Letters:", " ".join(guessed_letters) if guessed_letters else "None")
        print("Remaining Chances:", chances)

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter only one alphabet letter.")
            continue

        # Already guessed
        if guess in guessed_letters:
            print("⚠ You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        # Correct Guess
        if guess in secret_word:
            print("✅ Nice! Correct guess.")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess

        # Wrong Guess
        else:
            chances -= 1
            print("❌ Wrong guess!")

    # Result
    if "_" not in guessed_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word.upper())
    else:
        print("\n💀 Game Over!")
        print("The correct word was:", secret_word.upper())

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n😊 Thanks for playing Hangman!")
        break