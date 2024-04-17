#A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar
#Em alguumas linguagens manipular sequêcnais de caracteres não é um trabalho trivial, porém, em python esse
#trabalho é muito simples.

# Maíuscula, minúscula e título
curso = "PyThOn"

print(curso.upper())
#>>> PYTHON

print(curso.lower())
#>>> python

print(curso.title())
#>>> Python

print()
#Eliminando espaços em branco
curso = "  Python "

print(curso.strip())
#>>> "Python"

print(curso.lstrip())
#>>> "Python "

print(curso.rstrip())
#>>> "  Python"

print()
#Junções e centralização
curso = "Python"

print(curso.center(10, "#"))
#>>> "##Python##"

print(".".join(curso))
#>>> "P.y.t.h.o.n

#INTERPOLAÇÃO DE VARIÁVEIS#

#Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, 
#a segunda é utilizando o método format e a última é utiliznado f strings.
#A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro.

#Old Style %

nome = "Pedro"
idade = 17
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso %s." %(nome, idade,profissao, linguagem))
#>>> Olá, me chamo Pedro. Eu tenho 17 anos de idade, trabalho como Programador e estou matriculado no curso Python.
print()
#Método format
nome = "Pedro"
idade = 17
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso {}." .format(nome, idade,profissao, linguagem))
#>>> Olá, me chamo Pedro. Eu tenho 17 anos de idade, trabalho como Programador e estou matriculado no curso Python.
print()
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso {0}." .format(linguagem, profissao, idade, nome))
#>>> Olá, me chamo Pedro. Eu tenho 17 anos de idade, trabalho como Programador e estou matriculado no curso Python.
print()
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso {linguagem}." .format(nome = nome, idade = idade,profissao = profissao, linguagem = linguagem))
#>>> Olá, me chamo Pedro. Eu tenho 17 anos de idade, trabalho como Programador e estou matriculado no curso Python.
print()
#print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso {linguagem}." .format(**pessoa))
#>>> Olá, me chamo Pedro. Eu tenho 17 anos de idade, trabalho como Programador e estou matriculado no curso Python.
#print()

#F-string

nome = "Pedro"
idade = 17
profissao = "Programador"
linguagem = "Python"
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso {linguagem}.")

#Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")
#>>> "Valor de PI: 3.14"
print()

print(f"Valor de PI: {PI:10.2f}")
#>>> "Valor de PI:       3.14"
print()

#FATIAMENTO DE STRINGS#

#É uma técnica utilizada para retornar substrings (partes de string original), informando 
#ínicio(start), fim(stop) e passo(step): [start: stop[,step]].

nome = "Pedro Vieira Marques"

print(nome[0])
#>>> "P"
print()

print(nome[:5])
#>>> "Pedro"
print()

print(nome[10:])
#>>> "ra Marques"
print()

print(nome[10:13])
#>>> "ra"
print()

print(nome[10:13:2])
#>>> "r"
print()

print(nome[:])
#>>> "Pedro Vieira Marques"
print()

print(nome[::-1])
#>>> "seuqraM arieiV ordeP"

#String Múltiplas linhas#

#Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição.
#Elas podem ocupar várias linhas de código, e todos os espaços em branco são incluídos na string final.

#Strings triplas
nome = "Pedro"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""
#>>>
#
#Olá meu nome é Pedro,
#Eu estou aprendendo Python

#NÃO TEM DIFERENÇA ENTRE USAR ASPAS SIMPLES -> '' OU USAR ASPAS DUPLAS -> ""#

#Outro Exemplo que mostra a praticidade desse método

print(
    """
====== MENU ======

1 - depositar 
2 - sacar
0 - sair

==================
    """
)

#Se torna mais fácil criar Menus como esse, pois, sem esse método, teriamos que fazer linha por linha.

