# Aula 20 - Type Error, Type Cheking and Type Conversion

# Usando o num_char diretamente dentro de uma careia de caracteres apresenta um erro do tipo
# TypeError: can only concatenate str (not "int") to str.
num_char = len(input("What is your name?\n"))
#print("Your name has " + num_char + " characters.")

# Usando a função type para checar o tipo da variavel:
print(type(num_char))

# Usando a função str para converter um valor em string:
num_char = str(num_char)

# Usando a função type para checar o tipo da variavel:
print(type(num_char))

# Imprimindo, agora sim, corretamento o número de caracteres do nome:
print("Your name has " + num_char + " characters.")

# Exemplo de definação de uma variável e alteração do seu tipo:

a = 12
print(a)
print(type(a))
a = str(a)
print(type(a))

b = True
print(b)
print(type(b))
b = str(b)
print(type(b))

c = 123
print(c)
print(type(c))
c = float(c)
print(type(c))

d = 123.5
print(d)
print(type(d))
d = str(d)
print(type(d))