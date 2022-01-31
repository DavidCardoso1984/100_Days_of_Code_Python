#Password Generator Project
from posixpath import split
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
list_characterer = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
print(nr_letters) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
print(nr_letters)
nr_numbers = int(input(f"How many numbers would you like?\n"))
print(nr_numbers)
list_of_nr = [nr_letters, nr_symbols, nr_numbers]
print(list_of_nr)
total_of_nr = nr_letters + nr_symbols + nr_numbers
print(total_of_nr)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Para solução do problema;

# Saber quantos cada tipo de caractere o usuário quer, ou seja, quantos de cada lista; Ok
# Depois de usar um destes caracteres é necessario descontar da quantidade de caractere de cada lista;
# Deve-se selecionar uma das listas aleatoriamente e um elemento de cada lista aleatoriamente.
    # aqui pode-se criar uma lista com as listas;
# Guardar cada um dos itens em uma lista ou variável.

password = []

for nr in range(0 ,total_of_nr):
    # Sorteio de uma das três listas disponíveis:
    list_of_nr_sort = random.randint(0, 2)
    # Sorteando o número do componente da lista sorteada:
    list_of_nr_character_sort = random.randint(0, len(list_characterer[list_of_nr_sort])-1)
    print(list_of_nr_character_sort)
    # Selecionadno o componente da lista sorteada:
    character_sort = list_characterer[list_of_nr_sort][list_of_nr_character_sort]

    # Checando se a lista selecionada contém a quantidade informada pelo usuário maior que zero e descontando
    # em um esse valor.
    print(list_of_nr[list_of_nr_sort])
    if list_of_nr[list_of_nr_sort]>=0:
        password.append(character_sort)
        list_of_nr[list_of_nr_sort] -= 1
    else:
        total_of_nr += 1

#if total_of_nr != 0:

print(f"Here is the password: {password}")
