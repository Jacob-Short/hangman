from ascii_art import logo
import random

from words_list import word_list


hidden_words = random.choice(word_list)
word_length = len(hidden_words)

end_of_game = False
lives = 6

print(logo)

print(f'Pssst, the solution is {hidden_words}.')

# Creating the blank lines to represent letters
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user enters letter that they have already guessed, print the letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check the guessed letter
    for position in range(word_length):
        letter = hidden_words[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in hidden_words:
        # If the letter is not in the hidden_words, print out the letter and let them know it's not in the word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all elements in list and turn it into a string
    print(f"{' '.join(display)}")

    # Check if user has all letters correct
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from ascii_art import stages
    print(stages[lives])
