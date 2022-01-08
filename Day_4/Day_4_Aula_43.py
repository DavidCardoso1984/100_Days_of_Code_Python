# Day 4 - Aula 43 - Understading the Offset and Appending items to Lists

# Listas são estrutura de dados padrões;
# São uma forma de organizar e armazenar dados em python.

# Quando queremos armazenar somente um valor podemo usar variaveis simples:
a = "teste"
type_a = type(a)
print(f'Temos "a" com o valor de {a}, uma variável simples do tipo {type_a}.')

b = 21
type_b = type(b)
print(f'Temos "b" com o valor de {b}, uma variável simples do tipo {type_b}.')

# Quando queremos armazenar dados que tem alguma relação entre si, dentro de uma mesma variável podemos usar
# as listas.

# As estrutura de dados tem características próprias, como as listas permitem ser usadas para registrar 
# a sequência da chegada de dados.

# Exemplo:
fruits = ["Cherry", "Apple", "Pear"]
numbers = [1, 2, 3]

print(fruits)
print(numbers)

states_of_america = ['Delaware','Nova Jérsei','Pensilvânia','Carolina do Sul','Conecticute',
                    'Geórgia','Marilândia','Massachusetts','Nova Hampshire','Nova Iorque',
                    'Virgínia','Carolina do Norte','Ilha de Rodes','Vermonte','Kentucky',
                    'Tenessi','Ohio','Luisiana','Indiana','Mississípi','Ilinóis','Alabama',
                    'Maine','Missúri','Arcansas','Míchigan','Flórida','Texas','Iowa','Wisconsin',
                    'Califórnia','Minesota','Óregon','Cansas','Virgínia Ocidental','Nevada','Nebrasca',
                    'Colorado','Dakota do Norte','Dakota do Sul','Montana','Washington','Idaho',
                    'Wyoming','Utá','Oclaoma','Arizona','Novo México','Alasca','Havaí',]

# As listas seguem uma ordem de inclusão, o item mais recente a ser incluido vai para o fim da lista. 
# Isso é uma propriedade interessante que pode ser utilizada quando necessário.

# imprimindo um dos componentes da lista.
# Item na psoição zero:
print(states_of_america[0])

data_position = states_of_america[2]
print(data_position)

# Se usarmos indeces negativos a contagem começa no fim da fila:
print(states_of_america[-1])
print(states_of_america[-2])

# Para alterar um dos itens da lista temos que indicar o nome da lista e a posição que queremos
# substituir:
states_of_america[2] = "Pennsylvania"
print(states_of_america[2])

# Para incluir um item a uma lista usamos a funão append. Observar que o item é adicionado ao fim da lista:
states_of_america.append("Davidland")
print(states_of_america[-1])

# Para incluir um item em uma posição especifica podemos usar a função insert:
states_of_america.insert(0,"Enzolandia")

# Para adcionar multiplos itens na lista temos que usar a função extend:
states_of_america.extend(["Sabrinaland", "Joazinholand"])
print(states_of_america)

# Acessando um intervalo de dados em uma lista:
print(states_of_america)
print(states_of_america[0:2])
#Para imprimir o ultimo elemento da lista:
print(states_of_america[-1])
# Para imprimir do ultimo elemento para traz:
print(states_of_america[-4:])