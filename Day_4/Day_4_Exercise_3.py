# Dia 4 - Exercise 3 - Treasure Map

# Instructions

# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.

# Your job is to write a program that allows you to mark a square 
# on the map using a two-digit system. The first digit is the vertical 
# column number and the second digit is the horizontal row number. e.g.

# First, your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".

# Hint
# Remember that Lists start at index 0!
# map is just a variable that contains a nested list. 
# It's not related to the map function in Python.

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Separando a informação do usuário por linha e coluna:
position_row = int(position[0])-1
position_col = int(position[1])-1

# Definindo o local do X no mapa:
map[position_row][position_col] = "X"

# Imprimindo o mapa:
print(f"{row1}\n{row2}\n{row3}")

# A parte que torna fácil a solução desse problema é que a função 
# input retorna uma string, e é possível tratar uma string como um vetor.
# Assim fica fácil separar o npumero informado pelo usuário em duas partes.

