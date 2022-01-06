# Aula 29 - Control Flow with if / else anda Conditional Operators.

# Condicionais:
# Exemplo do uso de válcula de transbordo de uma banheira;
# if/else;

# Exemplo:

# if condition:
#     do this 
# else:
#     do this

# water level = 50
# if water level > 80:
#     print("Drain water") 
# else:
#     print("Continue")

# Exemplo rollercoaster:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


# Teste lógico básico, alguns pontos de atenção são não esquecer de 
# usar : depois dos testes lógicos e cuidar com a identação (IdentationError), 
# como já mencionado no Python isso é muito importante.
if height > 120:
    print("You can ride the rollercoaster!")
    # Tudo aqui faz parte
    # do bloco de código que
    # será executado se a condição
    # do if for verdadeira.
else:
    print("Sorry, you have to grow taller before you can ride!")
    # Tudo aqui faz parte
    # do bloco de código que
    # será executado se a condição
    # do else for verdadeira.

# Comparison Operators

# Operator   Meaning
# >          Maior que/Greater than 
# <          Menor que/Less than
# >=         Maior ou igual/Greater than or equal to 
# <=         Menor ou igual/Less than or equal to     
# ==         Igual/Equal to 
# !=         Diferente/Not equal to

# Observação o sinal de "=" sozinho equivale a atribuir um valor a uma variável.
# equanto "==" é equivalente a fazer uma verificação de igualdade (SintaxError). 