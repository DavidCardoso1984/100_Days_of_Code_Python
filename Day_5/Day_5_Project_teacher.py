#Password Generator Project
from posixpath import split
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


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

# Eazy level
# Definindo o password como uma string:
password = ""

# Sortenando as letras:
for char in range(1 , nr_letters+1):
    password += random.choice(letters)

# Sortenando os números:
for num in range(1 , nr_numbers+1):
    password += random.choice(numbers)

# Sortenando os simbolos:
for sym in range(1 , nr_symbols+1):
    password += random.choice(symbols)

# Imprimindo o password:
print(f"Here is the password: {password}")

# Hard level

#Definindo o password como uma lista:
password_list = []

# Sortenando as letras:
for char in range(1 , nr_letters+1):
    password_list.append(random.choice(letters))

# Sortenando os números:
for num in range(1 , nr_numbers+1):
    password_list.append(random.choice(numbers))

# Sortenando os simbolos:
for sym in range(1 , nr_symbols+1):
    password_list.append(random.choice(symbols))

# Embaralhando os valores sorteados:
random.shuffle(password_list)

# Transformando a lista em uma string:
password_char = ""
for char in password_list:
    password_char += char

# Imprimindo o password:
print(f"Here is the password: {password_char}")
