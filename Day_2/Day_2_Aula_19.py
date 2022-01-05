# Aula 19 - Python Primitive Data Types

# Usando a função len para verificar o compimento de uma string:
print(len("Hello"))

# A função len não funciona para números inteiros, o exemplo abaixo
# vai gerar um erro de TypeError: object of type 'int' has no len():
#print(len(12345))

# Tipos de dados primitivos no Python: String, Integer, Float, Boolean.

# ****Strings****

# São textos que estão entre aspas simples ou duplas;
# São uma sequência de caracters;

"Hello"
'Hello'

# Imprimindo somente o primeiro caractere de uma string:
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

# Números também podem ser strings:
print("123" + "456")

# O + usado com strings tem a função de concatenar textos.

# **** Integer ****

# Somente digitar numero faz com que o Pytho entenda esses valores como números inteiros:
123
print(123)

# Imprimindo o tipo de um valor:
print(type(123))

# Imprimindo a soma de números inteiros:
print(123+345)

# O _ serve para separação de milhares no Python
123_456_678
print(123_456_678)
print(type(123_456_678))

# **** Float ****

# São as frações.

3.14159
print(3.14159)
print(type(3.14159))

# **** Bolean ****

# Valores booleanos.

True
False

print(type(True))