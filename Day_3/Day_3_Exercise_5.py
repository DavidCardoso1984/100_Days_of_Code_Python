# Exercise 5 - Love Calculator

# 💪 This is a Difficult Challenge 💪

# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# Hint
# The lower() function changes all the letters in a string to lower case.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

# The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

# 🚨 Don't change the code below 👇

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Colocando todos os nome em letra minuscula:
name1_lower = name1.lower()
name2_lower = name2.lower()

# Existe formas melhores de construi esse código, usando iterações por exemplo, 
# porém com os recursos apresentado até o momento do curso acredito que seja o caminho
# que a professora espera que seja seguido.

# Checando o número de vezes que as letras de TRUE aparecem nos dois nomes:
# para name1:
t_count = name1_lower.count("t")
r_count = name1_lower.count("r")
u_count = name1_lower.count("u")
e_count = name1_lower.count("e")
true_count = t_count + r_count + u_count + e_count

# para name2:
t_count = name2_lower.count("t")
r_count = name2_lower.count("r")
u_count = name2_lower.count("u")
e_count = name2_lower.count("e")
true_count += t_count + r_count + u_count + e_count

# Checando o número de vezes que as letras de LOVE aparecem nos dois nomes:
# para name2:
l_count = name1_lower.count("l")
o_count = name1_lower.count("o")
v_count = name1_lower.count("v")
e_count = name1_lower.count("e")
love_count = l_count + o_count + v_count + e_count

# para name2:
l_count = name2_lower.count("l")
o_count = name2_lower.count("o")
v_count = name2_lower.count("v")
e_count = name2_lower.count("e")
love_count += l_count + o_count + v_count + e_count

# Calculando o score:
score = int(str(true_count) + str(love_count))

# Aplicando a regra para cada pontuação de score:

if score<=10 or score>=90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")