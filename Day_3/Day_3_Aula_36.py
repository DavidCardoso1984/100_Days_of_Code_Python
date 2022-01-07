# Day 3 - Aula 36 - Logical Operators

# Avaliando estrura lógica básica:
# if condition:
#     do A
# else:
#     do B

# Avaliando estrura lógica com mais de uma condição:
# if condition1 & condition2 & condition3:
#     do A
# else:
#     do B

# Operadores lógicos:
# and -> A and B
# or  -> C or D
# not -> not E

# Exemplo tabela verdade básica:

# and
# True and True -> True
# False and True -> False
# True and False -> False
# False and False -> False

# or
# True or True -> True
# False or True -> True
# True or False -> True

# not
# not True -> False
# not False -> True

# Exemplo Rollercoaster com dois if aninhados:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are R$ 5,00")
    if age <= 18:
        bill = 7
        print("Youth tickets are R$ 7,00")
    if age <45:
        bill = 12
        print("Adult tickts are R$ 12,00")
    if age >=45 or age <=55:
        bill = 0
        print("Senior tickts are R$ 0,00")

    wants_photo=input("Do you want a photo taken? Y or N\n")
    if wants_photo == "Y":
        bill += 3

    print(f"You final bill is R$ {bill}.")    


else:
    print("Sorry, you have to grow taller before you can ride!")