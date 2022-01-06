# Aula 22 - Mathematical Operations in Python

# Adição
print("Adção:")
7 + 5
5 + 13
18 + 4

# Subtração
print("Subtração:")
7 - 5
5 - 13
18 - 4

# Divisão
# Divisão sempre vai resultar em um float, mesmo que não tenha um resto da divisão. 
print("Divisão:")
print(6/2)
print(type(6/2))
print(6/4)
print(type(6/4))

# Potenciação
print("Potenciação")
print(2**2)
print(2**3)
print(2**4)
print(2**1.5)
print(16**0.5)
print(16**-0.5)

# Ordem de prioridade de operações matemáticas.
# No curso essa ordem de prioridade é chamado de PEMDAS.

# 1 - P. Parenteses;
# 2 - E. Expoentes;
# 3 - M. Mulplicação;
# 4 - D. Divisão;
# 5 - A. Adição;
# 6 - S. Subtração

# 1 - P. ();
# 2 - E. **;
# 3 - M. *;
# 4 - D. /;
# 5 - A. +;
# 6 - S. -

# Destas operações algumas tem igualdade na prioridade:
# 1 - ();
# 2 - **;
# 3 - * e /;
# 4 - + e -;

# Exemplo do PEMDAS:

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(3 * 3 + 3 / 3 ** 3)