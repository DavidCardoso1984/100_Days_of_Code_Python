#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
list_characterer = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
list_of_nr = [nr_letters, nr_symbols, nr_numbers]
total_of_nr = nr_letters + nr_symbols + nr_numbers

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Here is the password: ")

# Para solução do problema;

# Saber quantos cada tipo de caractere o usuário quer, ou seja, quantos de cada lista; Ok
# Depois de usar um destes caractere é necessario descontar da quantidade de caractere de cada lista;
# Deve-se selecionar uma das listas aleatoriamente e um elemento de cada lista aleatoriamente.
    # aqui pode-se criar uma lista com as listas;
# Guardar cada um dos itens em uma lista ou variável.

for carachter in range(0, total_of_nr + 1):
    random_list_characterer = [random.randint(0, 2)]
    if list_characterer[random_list_characterer]>0:

    password = 
