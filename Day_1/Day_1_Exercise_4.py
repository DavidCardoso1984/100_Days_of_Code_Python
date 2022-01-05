# Exercise 4 - Variables

# Instructions
# Write a program that switches the values stored in the variables a and b.

# Warning. Do not change the code on lines 1-4 and 12-18. Your program should 
# work for different inputs. e.g. any value of a and b.

# Minha solução:

# Recebendo o input do usuário:
a = input('a: ')
b = input('b: ')

# Fazendo a inversão das variáveis:
a1 = b
b1 = a

a = a1
b = b1

# Imprimindo as variáveis invertidas:
print("a: " + a)
print("b: " + b)

# Solução da professora:

# Recebendo o input do usuário:
a = input('a: ')
b = input('b: ')

# Fazendo a inversão das variáveis:
c = a
a = b
b = c

# Imprimindo as variáveis invertidas:
print("a: " + a)
print("b: " + b)