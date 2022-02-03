# Aula 77 - Improving the User Experience

# Importando módulos do python
import hangman_art, hangman_words, random

from replit import clear

# Imprimindo o logo para o usuário
print(hangman_art.logo)

# Buscando a nova lista de palavras:
word_list = hangman_words.word_list

# Buscando as astes:
stages = hangman_art.stages

# Defininfo o número de vidas igual ao comprimento
# do stages:
lives = len(stages)

# Selecionando uma palavra da lista:
chosen_word = random.choice(word_list)

# Criando a lista chamada display e guessed:
guessed = []
display = []
for letter in chosen_word:
    display.append("_")

# Definindo o loop para prenchimento da palavra
value_ = display.count("_")

while "_" in display and lives>1:
    #Solicitando ao usuário uma letra:
    guess = input("Guess a letter:\n").lower()

    # Limpando o terminal:
    clear()
    
    if guess not in guessed:
        if guess not in chosen_word:
            print("Não consta na palavra sorteada a letra: ", guess)
        for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess


        if  display.count("_") == value_:
            lives -= 1
        else:
            value_ = display.count("_")

        value_ = display.count("_")
    else:
        print("Você ja informou a letra: ", guess)
    
    guessed.append(guess) 
    print(display)
    print(stages[lives-1])

# Verificando se o usuário ganhou ou perdeu o jogo:
if lives > 1:
    print("You win!")
else:
    print("You lose!")