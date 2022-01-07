# Day 3 - Exercise 2 - BMI Calculator

# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height;
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and 
# a short person both weigh the same amount, the short person is usually more overweight;
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m);
# Fórmula: BMI = weight/heigth^2;

# It should tell them the interpretation of their BMI based on the BMI value:
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Hint
# Check the data type of the inputs;
# Try to use the exponent operator in your code;
# Remember to round your result to the nearest whole number.
# Remember PEMDAS;
# Remember to convert your result to a whole number (int).
# Make sure you include the words in bold from the interpretations.

# Solicitando as informações do usuário:
height = float(input("Enter your height:\n")) # Não esquecer que o retorno do input é uma string!
weight = float(input("Enter your weight:\n")) # Não esquecer que o retorno do input é uma string!

# Minha solução:
# Calculando o BMI>
BMI = round(weight/height**2,0)
BMI = int(BMI)

# Definindo em qual grupo o usuário se encaixa:
if BMI<18.5:
    BMI_interpretion="are underweight"
else:
    if BMI<25:
        BMI_interpretion="have a normal weight"
    else:
        if BMI<30:
            BMI_interpretion="are slightly overweight"
        else:
            if BMI<35:
             BMI_interpretion="are obese"
            else:
             BMI_interpretion="are clinically obese"

# Imprimindo os resultados:
print(f"Your BMI is {BMI}, you {BMI_interpretion}.")

# solução da instrutora:
# Calculando o BMI>
BMI = round(weight/height**2,0)

# Definindo em qual grupo o usuário se encaixa:
if BMI<18.5:
    BMI_interpretion= print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<25:
    BMI_interpretion= print(f"Your BMI is {BMI}, have a normal weight.")
elif BMI<30:
    BMI_interpretion= print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI<35:
    BMI_interpretion= print(f"Your BMI is {BMI}, you are obese.")
else:
    BMI_interpretion= print(f"Your BMI is {BMI}, you are are clinically obese.")
