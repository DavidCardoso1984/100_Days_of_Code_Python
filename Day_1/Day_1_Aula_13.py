# A aula 13 Python Variables. Explicação sobre o uso de variáveis no Python.

# Guardando o nome fornecido pelo usuário dentro de uma variável chamada name:
name = input("What is your name?\n")
print("Hello " + name + "!")

# Verificar como o programa é executado e vai substituindo o valor da variável name:
name = "Pedro"
print("Hello " + name + "!")

name = "Angela"
print("Hello " + name + "!")

# Atribuindo o tamanho da string dentro de variável chamada length:
name = input("What is your name?\n")
length = len(name)
print (length)

# Para colocar a variavel length dentro de uma string é necesspario convertela:
length_string = str(length)
print("The length of the name " + name + " is " + length_string + ".")
