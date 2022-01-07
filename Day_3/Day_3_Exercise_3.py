# Day 3 - Exercise 2 - Leap Year (Ano bissexto)


#--------------------------------------------------------------------------------#

# Consulta na internet sobre anos bissextos:

# https://docs.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year

# 1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# 2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# 3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# 4. O ano é bissexto (tem 366 dias).
# 5. O ano não é um ano bissexto (tem 365 dias).

#--------------------------------------------------------------------------------#

# Instructions

# Write a program that works out whether if a given year is a leap year. A normal 
# year has 365 days, leap years have 366, with an extra day in February. The reason 

# why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Hint
# Try to visualise the rules by creating a flow chart on www.draw.io
# If you really get stuck, you can see the flow chart I created:
# https://bit.ly/36BjS2D

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result_4 = int(year%4)
result_100 = int(year%100)
result_400 = int(year%400)

if result_4==0:
    if result_100==0: # Se o resto da divisão por 4 for igual a 0;
        if result_400==0: # Se o resto da divisão por 100 for igual a 0;
            print('Leap year.') # Se o resto da divisão por 400 for igual a 0;
        else:
            print('Not Leap year.') # Se o resto da divisão por 400 for igual a 0;
    else:
        print('Leap year.') # Se o resto da divisão por 100 não for igual a 0; 
else:
        print('Not leap year.') # Se o resto da divisão por 4 não for igual a 0;