# Day 7 - Aula 71 - Replacing Blanks with Guesses

# Step 1:

word_list = ["ardvark", "baboon", "camel"]

# ToDo_1 - Randomly choose a word from the word_list and
# assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

# testinf code
print(f'Pssst, the solution is {chosen_word}.')

# ToDo_2 - Ask the user to guess a letter and assign their
# answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter:\n").lower()

# ToDo_3 - Check it the letter the user guessed (guess) is
# one pf the leters in the chosen_word.

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# Step 2:

# ToDo_1 - Create an empty List called display.
# For each letter in the chosen_word, add a "_"
# to 'display'.
# So if the chosen word was "apple", display should be
# ["_","_","_","_","_"] with 5 "_" representing each letter
# to guess.

display = []
for letter in chosen_word:
    display.append("_")

print(display)

# ToDo_2 - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal
# that letter in the display at the position.
# e.g If the user guessed "p" and the chosen word was "apple",
# then display should be ["_", "p", "p", "_", "_"].

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess
        

# ToDo_3 - Print 'display' and you should see the guessed letter in
# the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to gues the next letter. 
# We'll tackle that in step 3.

print(display)
