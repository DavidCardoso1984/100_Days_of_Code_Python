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

# Determinando a seleção do computador:

# Importando o módulo random e definindo a seleçao do computador:
import random
comp_selection = random.randint(0,2)

# Definindo o ganhador:
if user_selection>=3 or user_selection<0: 
    print("Você não selecionou uma opção correta!\n")
elif options[user_selection] == rock and options[comp_selection] == scissors:
    print("You win!")
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
elif options[user_selection] == rock and options[comp_selection] == paper:
    print("You lose!")
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
elif options[user_selection] == scissors and options[comp_selection] == paper:
    print("You win!")
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
elif options[user_selection] == scissors and options[comp_selection] == rock:
    print("You lose!")
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
elif options[user_selection] == paper and options[comp_selection] == rock:
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
    print("You win!")
elif options[user_selection] == paper and options[comp_selection] == scissors:
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
    print("You lose!")
elif options[user_selection] == options[comp_selection]:
    print(f"A sua seleção foi: {options[user_selection]}")
    print(f"A seleção do computador foi: {options[comp_selection]}")
    print("o jogo ficou empatado!")

print("Fim de jogo!")

# Opção proposta pela orienatadora:

# Se tivermos 0 para Rock, 1 para Paper or 2 para Scissors

if user_selection==0 and comp_selection==2:
    print("You win!")
elif comp_selection == 0 and user_selection == 2:
    print("You loose!")
elif comp_selection==user_selection:
    print("It's a draw!")
elif user_selection >=3 or user_selection < 0:
    print("You typed an invalid number, you lose!")
elif comp_selection>user_selection:
    print("You lose!")
elif comp_selection<user_selection:
    print("You lose!")


# Existem melhorias para redução do número de lisnhas deste projeto.