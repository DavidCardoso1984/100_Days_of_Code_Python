# Day 2 - Project Tip Calculator

# Instructions:
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input:
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Example Output:
# Each person should pay: $19.93

# Hint:
# How to round a number to 2 decimal places in Python
# How to limit a float to two decimal places in Python

# Resolução:

# Exibindo mensagem de inicio:
print("Welcome to the tip calculator!")

# Solicitando, convertendo e armazenando o valor total da conta:
total_bill=round(float(input("What was the total bill? $")),2)

# Solicitando, convertendo e armazenando o valor da gorjeta:
tip_value=int(input("How much tip would you like to give? 10, 12, or 15?"))

# Solicitando, convertendo e armazenando o valor da gorjeta:
split_value=int(input("How many people to split the bill?"))

# Calculando o valor que cada pessoa deve pagar:
total_bill_tip = round(total_bill*(1+tip_value/100),2)
total_bill_split = round(total_bill_tip/split_value,2)

# Imprimindo o valor individual:
print(f"Each person should pay: ${total_bill_split}")