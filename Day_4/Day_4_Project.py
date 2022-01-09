# Day 4 - Project: Rock, Paper Scissors

# Instructions
# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a 
# corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

# Definindo os desenhos ASCII:

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Colocando em uma lista as opções:
options = [rock, paper, scissors]

# Abertura do jogo:
print("Hello to the Rock, Paper Scissors' Game!")

# Pedindo para o usuário fazer a sua seleção:
user_selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_selection = int(user_selection)

# Exibindo a escolha do usuário:
print(f"A sua seleção foi: {options[user_selection]}")

# Determinando a seleção do computador:

# Importando o módulo random e definindo a seleçao do computador:
import random
comp_selection = random.randint(0,2)

# Imprimindo a seleção do computador:
print(f"A seleção do computador foi: {options[comp_selection]}")

# Definindo o ganhador:

if options[user_selection] == rock and options[comp_selection] == scissors:
    print("You win!")
elif options[user_selection] == rock and options[comp_selection] == paper:
    print("You lose!")
elif options[user_selection] == scissors and options[comp_selection] == paper:
    print("You win!")
elif options[user_selection] == scissors and options[comp_selection] == rock:
    print("You lose!")
elif options[user_selection] == paper and options[comp_selection] == rock:
    print("You win!")
elif options[user_selection] == paper and options[comp_selection] == scissors:
    print("You lose!")
elif options[user_selection] == options[comp_selection]:
    print("o jogo ficou empatado!")
else:
    print("Você não selecionou uma opção correta!\n")

print("Fim de jogo!")