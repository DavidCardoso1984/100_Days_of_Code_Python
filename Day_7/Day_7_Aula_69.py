# Day 7 - Aula 69 - Picking a Random Words And Cheking Answer

# Step 1:

word_list = ["ardvark", "baboon", "camel"]

# ToDo_1 - Randomly choose a word from the word_list and
# assign it to a variable called chosen_word.

# ToDo_2 - Ask the user to guess a letter and assign their
# answer to a variable called guess. Make guess lowercase.

# ToDo_3 - Check it the letter the user guessed (guess) is
# one pf the leters in the chosen_word. 

# Importar a biblioteca randon:
import random

# Selecionar uma palavra:
# A opção abaixo funciona, mas temos um função dentro da 
# bilbioteca random que faz isso de forma mais simples.
# chosen_word = word_list[random.randint(0,2)]
chosen_word = random.choice(word_list)

# Pedir ao usuário uma letra e guarda-la em uma variável:
guess = input("Guess a letter:").lower()

# for i in range(0, len(chosen_word)):
#     if guess == chosen_word[i]:
#         print(True)
#     else:
#         print(False)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
