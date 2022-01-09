# Day 4 - Exercise 2 - Banker Roulette

# Instructions
# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a 
# List called names. For this to work, you must enter all the names as names followed by comma then space. 
# e.g. name, name, name
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, 
# it's only for our testing code to check your work.

# Hint
# You might need the help of the len() function.
# https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

# Remember that Lists start at index 0!


# 🚨 Don't change the code below 👇
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Determinando o tamanho da lista:
length = len(names)
indice = length-1

#Fazendo o sorteio aleatorio do indice da lista:
sorteado = random.randint(0,indice)
print(f"{names[sorteado]} is going to buy the meal today!")

# Uma opção para esta lição seria o uso da função choice()
sorteado_choice = random.choice(names)
print(f"{sorteado_choice} is going to buy the meal today!")

linguagens = ["Ruby", "Python", "Java", "PHP", "C", "JavaScript"]
sorteado_linguagens = random.choice(linguagens)
print(sorteado_linguagens)
