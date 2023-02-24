# HANGMAN CHALLENGE 

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

print(display)

end_of_game = False
#test
while end_of_game == False:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(f"The word was {chosen_word}")

    # if guess in chosen_word:
    #     print(f"Well done. {guess} was in the word!")


    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])


        

