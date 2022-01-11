# Dia 5 - Exercício 2 - High Score

# Instructions
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

# Hint
# Think about the logic before writing code. How can you compare numbers against each other to see which 
# one is larger?

# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to 
# check your solution.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

n_max = 0

for n in student_scores:
    if n_max<n:
        n_max = n

print(f"The highest score in the class is: {n_max}")


# O Exercício poderia ter sido resolvido usando a função max() e min(0), ou seja, máximo e mínimo.
# Porém o desáfio era fazer um loop que simularia esta função.
print(max(student_scores))

print(min(student_scores))

