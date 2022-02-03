# Day 7 - Aula 73 - Checking if the Player has Won

# Step 1:

word_list = ["ardvark", "baboon", "camel"]

# ToDo_1 - Randomly choose a word from the word_list and
# assign it to a variable called chosen_word.
import random

from pandas import isnull
chosen_word = random.choice(word_list)

# testinf code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

# Step 3

# ToDo_1 - Use a while loop to let the user guess again.
# The loop should only syop once the user has guessed all the
# letters in the chosen_word and "display" has no more
# blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter:\n").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

print("You win!")
