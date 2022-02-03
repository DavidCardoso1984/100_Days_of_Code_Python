# Day 7 - Aula 75 - Keeping Track of the Player's Lives

# Definindo uma lista de palavras
word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = len(stages)
print("Lives: ", lives)

# Importando a biblioteca randon:
import random

# Selecionando uma palavra da lista:
chosen_word = random.choice(word_list)

# ToDo_1 - Create a variable called 'lives' to keep track of the number
# of lives left.
# Set 'lives' to equal 6.

# Suporte para teste do código:
print(f'Pssst, the solution is {chosen_word}.')

# Criando a lista chamada display:
display = []
for letter in chosen_word:
    display.append("_")

# Definindo o loop para prenchimento da palavra

value_ = display.count("_")

while "_" in display and lives>1:
    guess = input("Guess a letter:\n").lower()
    
    for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess


    if  display.count("_") == value_:
        lives -= 1
    else:
        value_ = display.count("_")

    value_ = display.count("_")
    
    print(display)
    print(stages[lives-1])
    
if lives > 1:
    print("You win!")
else:
    print("You lose!")

# ToDo_2 - If guess is not a letter in the chosen_word, then
# reduce 'lives' by 1.
# If lives goes downs to 0 then the game should stop and it 
# should print "You lose."

# Join all elements in the list and turn it into a String.

# ToDo_3 - print the ASCII art from 'stages' that corresponds to the
# current number of 'lives' the user has remaining. 