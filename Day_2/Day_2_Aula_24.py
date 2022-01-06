# Aula 24 - Number Manipulation and F Strings in Python

# Exemplo de divisão com resto:
print(8/3)

# Imprimindo como int:
print(int(8/3))

# Arredondando valores usando a função round:
print(round(8/3,2))

# Exibindo somente a parte inteira de uma divisão:
print(8//3)

# Usando valores armazenados dentro de uma variável:
result = 4/2
result /=2
print(result)

# Exemplo de um contador:
score = 0
score += 1
print(score)
score -= 1
print(score)

# Quando se quer calcular um valor com base nele mesmo é possível usar os comandos:
# +=, -=, /= e *=
# Exemplo:

print("Avaliando os valores de i:")
i = 0
print(i)
i +=1
print(i)
i *=2
print(i)
i -=1
print(i)
i /=2
print(i)

# Usando o f-String:
print(f"Your score is {score}.")

# Exemplo usando o f-String.
height = float(input("Enter your height:\n")) # Não esquecer que o retorno do input é uma string!
weight = float(input("Enter your weight:\n")) # Não esquecer que o retorno do input é uma string!
BMI = int(weight/height**2)
print(f"Your BMI is {BMI}.")