# Day 3 - Exercise 4 - Pizza Order Practice

# Instructions
# Congratulations, you've got a job at Python Pizza. 
# Your first job is to build an automatic pizza order program.
 
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# Hint
# Think about what you've learnt about multiple if statements and
# see if you can reduce the number of lines of code while having the same functionality.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Definir uma variável conta que será atualizada cada vez que uma das opções
# for selecionda.
bill = 0

# Aplicando as regras de negócio:

# Com relação a tamanho:
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# Com relação a Pepperony:
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
if add_pepperoni == "Y":
    if size == "S":
        bill+= 2
    else:
        bill+= 3


# Com relação a Extra cheese:
# Extra cheese for any size pizza: + $1
if extra_cheese == "Y":
    bill+= 1

print(f"Your final bill is: ${bill}.")