import random

# Word list (you can expand this!)
words = ["dragon", "sorcerer", "treasure", "labyrinth", "wand", "castle", "goblin", "elixir"]

# Hangman-style dungeon stages
dungeon_stages = [
    """
       +----+
       |    |
       O    |
      /|\\   |     You're barely hanging on...
      / \\   |
            |
    =========""",
    """
       +----+
       |    |
       O    |
      /|\\   |     The dungeon grows colder...
      /     |
            |
    =========""",
    """
       +----+
       |    |
       O    |
      /|\\   |     A shadow passes behind you...
            |
            |
    =========""",
    """
       +----+
       |    |
       O    |
      /|    |     You hear footsteps...
            |
            |
    =========""",
    """
       +----+
       |    |
       O    |
       |    |     Something stirs in the dark...
            |
            |
    =========""",
    """
       +----+
       |    |
       O    |     The air grows heavy...
            |
            |
    =========""",
    """
       +----+
       |    |
            |     You're free... for now.
            |
            |
    ========="""
]

# Choose a word
word_to_guess = random.choice(words).lower()
guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = len(dungeon_stages) - 1

# Display function
def display_word():
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])

# Intro
print("🧙‍♂️ Welcome, brave soul! You find yourself in a dark dungeon.")
print("A magical force has bound you — guess the word to escape!")
print(f"You have {max_wrong_guesses} chances before you're trapped forever...\n")

# Game loop
while wrong_guesses < max_wrong_guesses:
    print(dungeon_stages[max_wrong_guesses - wrong_guesses])
    print(f"\n🔎 Word: {display_word()}")
    print(f"📜 Letters guessed: {', '.join(sorted(guessed_letters))}")
    guess = input("\n🔠 Choose a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Only a single letter, adventurer!\n")
        continue

    if guess in guessed_letters:
        print("🌀 You've already tried that one.\n")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        print("✨ A spark of hope! That letter is correct.\n")
    else:
        wrong_guesses += 1
        print("💥 The dungeon tightens its grip. That was wrong!\n")

    if all(letter in guessed_letters for letter in word_to_guess):
        print(f"\n🌟 You did it! The word was: {word_to_guess}")
        print("🏃‍♂️ You break free from the dungeon as the walls crumble behind you!")
        break
else:
    print(dungeon_stages[0])
    print(f"\n☠️ The final rune fades. The word was: {word_to_guess}")
    print("You are lost to the shadows of the dungeon forever...")

