# Aula 14 - Variable Naming

# Guardando o nome fornecido pelo usuário dentro de uma variável chamada name:
n = input("What is your name?\n")
print("Hello " + n + "!")

l = len(n)

# Para colocar a variavel length dentro de uma string é necesspario convertela:
length_string = str(l)
print("The length of the name " + n + " is " + length_string + ".")

# Algumas regras básicas sobre nomear variáveis:
# Mantenha seu codigo legivel, por isso o nome das variáveis devem fazer sentido;
# Opte por nomes que melhor descrevem uma variável, por exemplo n troque por name, l troque por length et;
# Variaveis com nomes conpostos usar o separador _, por exemplo user_name;
# Variáveis podem possuir números mas não podem começar com números, exemplo length_2 ou length_2 estão
# corretas porém 2length ou 2_length;
# Não usar palavras reservadas ou de funções como print, input, str etc.

