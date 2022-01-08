# Day 4 - Aula 41 - Random Module

# Computadores são máquinas deterministicas, pois realizam atividades repetitivas de uma forma total previsível.

# Python usa um método chamado Mersenne Twister para gerar pseudo números aleatórios.

# Nesse link temos uma explicação simples sobre o tema:
# https://pt.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators


#-----------------------------------------------------------------------------------------------#
# Explicação sobre o que é um módulo python:
# Módulos são conjuntos de programas criados com o objeto de resolver algo específico.
# É uma forma de modularizar programas prontos para uso do usuário, evitando a necessidade da 
# criação de código de forma desnecessária.

# Um exemplo seria o próprio módulo random.

# Exemplo de criação do módulo my_module e importação do mesmo:
import my_module

# Dando um print do valor de pi escrito no my_module:
print(f"Valor de pi:{my_module.pi}")

#-----------------------------------------------------------------------------------------------#

# Importando o módulo random
import random

# Criando um número aleatório inteiro entre 1 e 10:
random_integer = random.randint(1, 10)
print(f"O valor do número aleatório inteiro é: {random_integer}")


# Criando um número aleatório fracionário entre 0.0 e 1.0 (nunca será um):
random_float = random.random()
print(f"O valor do número aleatório fracionário é: {random_float}")

# E sequisermos um número fracionário de 1 a 10 (nunca sendo 10)?
random_float = random.randint(1, 10) * random.random()
print(f"O valor do número aleatório fracionário de 1 a 10 é: {random_float}")

# E sequisermos um número fracionário de 1 a 5 (nunca sendo 5)?
random_float = random.randint(1, 5) * random.random()
print(f"O valor do número aleatório fracionário de 1 a 5 é: {random_float}")

# E sequisermos um número fracionário de 1 a 5 (nunca sendo 5)?
random_float = 5 * random.random()
print(f"O valor do número aleatório fracionário de 1 a 5 é: {random_float}")

# Uso do random para o love score:
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")