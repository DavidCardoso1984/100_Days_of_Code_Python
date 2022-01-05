# A aula 11 (The Python Input Function) fala sobre o uso de funções, 
# cita como exemplo a função print() e demonsta o uso de uma Input 
# Function dentro do Python.

# Comparando a função print com a função input

# Uso da função print:
print("Uso da função print:")
print("What is your name?\n") # Não espera o retorno de um usuário. 

print("Uso da função input:")
# Uso da função Input (perceber que a função fica esperando um retorno do usuário no terminal):
input("What is your name?\n")

print("Uso da função input dentro de uma função print:")
# Uso da função Input (perceber que a função fica esperando um retorno do usuário no terminal).
# A função input() vai pegar a inserção do usuário no terminal e a função print() vai imprimir Hello o
# o retorno da função input() e !:
print("Hello " + input("What is your name?\n") + "!")


