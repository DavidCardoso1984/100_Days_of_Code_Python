# Day 4 - Aula 45 - IndexErrors and Working with Nested Lists.

# Um dos erros mais comuns ao trabalhar com listas é o IndexError: list index out of range.

states_of_america = ['Delaware','Nova Jérsei','Pensilvânia','Carolina do Sul','Conecticute',
                    'Geórgia','Marilândia','Massachusetts','Nova Hampshire','Nova Iorque',
                    'Virgínia','Carolina do Norte','Ilha de Rodes','Vermonte','Kentucky',
                    'Tenessi','Ohio','Luisiana','Indiana','Mississípi','Ilinóis','Alabama',
                    'Maine','Missúri','Arcansas','Míchigan','Flórida','Texas','Iowa','Wisconsin',
                    'Califórnia','Minesota','Óregon','Cansas','Virgínia Ocidental','Nevada','Nebrasca',
                    'Colorado','Dakota do Norte','Dakota do Sul','Montana','Washington','Idaho',
                    'Wyoming','Utá','Oclaoma','Arizona','Novo México','Alasca','Havaí',]

# Alterando o conteúdo do indice 1:
states_of_america[1] = 'Pennsylvania'

# Incluindo dois novos valores na minha lista:
states_of_america.extend(["Davidland", "Sabrinaland"])

# Imprimindo os dois ultimos valores da lista:
print(states_of_america[-2:])

# Imprimindo o comprimento da minha lista, ou seja, o numero de itens que contem a lista.
print(len(states_of_america))

# Simulando o erro de IndexError: list index out of range
#print(states_of_america[53])

# É necessário atenção pois comprimento ou número de itens de uma listas é diferente de indice ou
# posição de um elemento em uma lista.

# states_of_america tem 52 elementos na lista, porém seus indices vão de 0 a 51.

# Guarando o npumero de estados da America em uma variável e imprimindo o ultimo estado:
num_of_states = len(states_of_america)
print(states_of_america[num_of_states-1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Collard and mustard greens", 
#                 "Nectarines", "Apples", "Grapes", "Cherries", "Peaches", "Pears", 
#                 "Bell and hot Peppers", "Celery", "Tomatoes"]
# print(dirty_dozen)

# É possível criar listas de listas, veja que criar uma lista de frutas e verduras da dirty_dozen.

# Criando duas listas:
fruit = ["Strawberries", "Nectarines", "Apples", "Grapes", 
            "Cherries", "Peaches", "Pears"]

vegetables = ["Spinach", "Kale", "Collard and mustard greens", 
                "Bell and hot Peppers", "Celery", "Tomatoes"]

# Colocando as duas listas dentro de uma lista (nested lists ou listas alinhadas):
dirty_dozen = [fruit, vegetables]

# Imprimindo a lista dirty_dozen
print(dirty_dozen)

# Imprimindo cada uma das listas separadamente:
print(dirty_dozen[0])
print(dirty_dozen[1])

# Imprimindo um componente de cada uma das lista:
print(dirty_dozen[0][3])
print(dirty_dozen[1][4])