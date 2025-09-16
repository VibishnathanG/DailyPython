import random

# ASCII art logo for game start
HANGMAN_LOGO = """
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
"""

print(HANGMAN_LOGO)
print("\nWelcome to Hangman! Try to guess the word before the man is hanged!\n")

ascii_stage_hangman = [
    """\
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
    """\
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """\
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """\
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """\
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """\
      +---+
      |   |
          |
          |
          |
          |
    ========="""
]

# Expanded word list with categories
word_categories = {
    'animals': ['elephant', 'giraffe', 'penguin', 'dolphin', 'kangaroo'],
    'fruits': ['apple', 'banana', 'orange', 'mango', 'strawberry'],
    'countries': ['france', 'japan', 'brazil', 'egypt', 'canada']
}

# Let player choose category
print("\nChoose a category:")
for i, category in enumerate(word_categories.keys(), 1):
    print(f"{i}. {category.title()}")

while True:
    try:
        choice = int(input("\nEnter category number: "))
        if 1 <= choice <= len(word_categories):
            selected_category = list(word_categories.keys())[choice-1]
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a number.")

random_words = word_categories[selected_category]
selected_word = random.choice(random_words).lower()
selected_word_org = selected_word

print("\nCategory:", selected_category.title())
print(''.join(['_']*len(selected_word)))

puzzle_word = ['_']*len(selected_word)
life = 6
guessed_letters = set()  # Track guessed letters

while life > 0:
    print("\nGuessed letters:", ' '.join(sorted(guessed_letters)))
    input_char = str(input('Enter a character: ')).lower()
    
    # Input validation
    if not input_char.isalpha() or len(input_char) != 1:
        print("Please enter a single letter!")
        continue
    
    if input_char in guessed_letters:
        print("You already guessed that letter!")
        continue
        
    guessed_letters.add(input_char)
    
    if input_char not in selected_word:
        life -= 1
        print('\nIncorrect! ❌')
        print(''.join(puzzle_word))
        print(f'Lives remaining: {"❤️ " * life}')
    else:
        index_value = selected_word.index(input_char)
        puzzle_word[index_value] = input_char
        print('\nCorrect! ✅')
        print(''.join(puzzle_word))
        selected_word = selected_word.replace(input_char, '_', 1)
        print(f'Lives remaining: {"❤️ " * life}')
    
    if life == 0:
        print('\n💀 Game Over! The word was:', selected_word_org)
    if ''.join(puzzle_word) == str(selected_word_org):
        print('\n🎉 Congratulations! You won!')
        break
    
    print(ascii_stage_hangman[life])
