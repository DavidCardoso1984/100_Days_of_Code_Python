# Day 3 - Aula 34 - Multiple if Statements in Succession

# Analisando a estrutura if/elif/else
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# Analisano a estrutura de nultiple if
# if condition1:
#     do A
# if condition2:
#     do B
# if condition2:
#     do C

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
    else:
        bill = 12
        print("Adult tickts are R$ 12,00")
    
    wants_photo=input("Do you want a photo taken? Y or N\n")
    if wants_photo == "Y":
        bill += 3

    print(f"You final bill is R$ {bill}.")    


else:
    print("Sorry, you have to grow taller before you can ride!")