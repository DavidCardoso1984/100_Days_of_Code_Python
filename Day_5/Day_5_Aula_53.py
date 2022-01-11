# Day 5 - Aula 53 - for loops and the range() function

    # for item in list_of_items:
    #     do something to each  item

# Muitas vezes precisamos usar um loop sem ter uma lista.

# Pesquisar sobre Carl Gauss

# Usando a função range().

# range() é utilizada para determinar quantas vezes um loop deve ser repetido se 
# não tivermos uma lista:


    # for number in range(a, b):
    #     print(number)

# Exemplo do uso do range() sem a definição de um step:
for number in range(1, 10):
    print(number)

# Uso do range() com a definição de um step:
for number in range(1, 11, 3):
    print(number)

# Resolvendo o problema de somar os números até 100:
number_sum = 0
for number in range(1, 101):
    number_sum += number
    print(number_sum)