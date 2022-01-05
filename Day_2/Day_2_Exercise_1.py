# Day 2 - Exercise 1 - Data Types

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Minha solução:
# Convertendo cada uma das partes do numero em um inteiro:
parte_1 = int(two_digit_number[0])
parte_2 = int(two_digit_number[1])
print(parte_1+parte_2)

# Solução da professora:

# Checando como é armazenada a informação do usuário:
print(type(two_digit_number))

# Como é armazenada como string, no python é possível usar a opção abaixo:
first_digit = two_digit_number[0]
seconf_digit = two_digit_number[1]

# Convertendo as str em int e fazendo a soma dos valores:
result = int(first_digit) + int(seconf_digit)
print(result)