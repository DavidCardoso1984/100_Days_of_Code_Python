# Day 2 - Exercise 3 - Life in Weeks

# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little 
# time we actually have;

# https://waitbutwhy.com/2014/05/life-weeks.html;

# Create a program using maths and f-Strings that tells us how many days, weeks, months we
# have left if we live until 90 years old;

# It will take your current age as the input and output a message with our time left in this format;

# You have x days, y weeks, and z months left;

# Where x, y and z are replaced with the actual calculated numbers;

# Warning your output should match the Example Output format exactly, even the positions of the commas
# and full stops.

# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year;
# Try copying the example output into your code and replacing the relevant 
# parts so that the sentence is formated the same way.

# Solicitando a idade di usuário:
age = input("What is your current age?\n")

# Calculando a diferença entre a idade e espectativa de vida de 90 anos:
age = int(age) # transformando age de str para int
saldo_age = 90 - age

# Calculando quantas meses de vida:
months = saldo_age*12

# Calculando quantas semanas de vida:
weeks = saldo_age*52

# Calculando quantos dias de vida:
days = saldo_age*365 # Para o calculo deve ser utilizado ano.

# Imprimindo o resultado solicitado:
print(f"You have {days} days, {weeks} weeks and {months} months left.")