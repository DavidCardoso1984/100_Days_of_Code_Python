# Day 3 - Aula 31 - Nested (aninhados) is statements and elif statements.

# Verificar condições aninhadas.
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# Exemplo Rollercoaster com dois if aninhados:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay R$ 7,00")
    else:
        print("Please pay R$ 14,00")
else:
    print("Sorry, you have to grow taller before you can ride!")


# Exemplo Rollercoaster com o uso do Elif:

# Verificar condições aninhadas com elif
# if condition1:
#     do this
# elif condition2:
#         do this
# else:
#      do this


height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay R$ 5,00")
    elif age > 18:
        print("Please pay R$ 12,00")
    else:
        print("Please pay R$ 7,00")
else:
    print("Sorry, you have to grow taller before you can ride!")