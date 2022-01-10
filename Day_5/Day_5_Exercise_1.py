# Day 5 - Exercise 1 - Average Height

# Instructions
# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total 
# number of heights.

# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164

# Important You should not use the sum() or len() functions in your answer. 
# You should try to replicate their functionality using what you have learnt about for loops.

# Hint
# Remember to use the round() function to round the average height before you print it.
# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, 
# click submit to check your solution.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Definindo os contadores iniciais e os seus respectivos valores:
sum_heights = 0
num_heights = 0

# Fazendo um loop para somar a os valores das alturas e o número de alunos:

# Para cada altura dentro da lista de altura dos estudantes, some os valores das alturas e some
# o número de estudantes.

for heights in student_heights:
    sum_heights += heights
    num_heights += 1

# Calculando a média dos alunos:
mean_heights = int(round(sum_heights/num_heights,0))

# Imprimindo o valor da média:
print(mean_heights)