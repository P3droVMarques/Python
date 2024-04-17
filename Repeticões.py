#As Estruturas de Repetição são estruturas utilizadas para repetir um trecho de código um determinado número de vezes. 
#Esse número pode ser conhecido previamente ou determinado atravéz de uma expressão lógica.

#comando "For" é usado para pecorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezez que
#nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

texto = input("informe o texto: ")
Vogais = "AEIOU"

for letra in texto:
    if letra.upper() in Vogais:
        print(letra, end="")
print()

#For/else

texto = input("informe o texto: ")
vogais = "AEIOU"
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
print()
print("Laço finalizado")

#Range = é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um 
#ínicio(inclusivo) para um fim(exclusivo). Se usarmos range(i,j) será produzido:
#i, i+1, i+2, i+3, ..., j-1.
#Ela recebe 3 argumentos: Stop(obrigatório), Start(opcional) e Step opcional.

#range(stop) -> range object
#range(start, stop[, step]) -> range object

list(range(4))
# >>> [0,1,2,3] 

#Range com for

for numero in range(0,11):
    print(numero, end=" ")
# >>> 0 1 2 3 4 5 6 7 8 9 10
    print()
#Exibindo a tabuada de 5
for numero in range(0,51,5):
    print(numero, end=" ")
# >>> 0 5 10 15 20 25 30 35 40 45 50
print()
#While = ele é usado para repetir um bloco de código várias vezes.
#Faz sentido usar While quando não sabemos o número exato de vezes
#Que nosso bloco de código deve ser executado.

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: ")) 
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
#While / else
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")

#break corta o laço a partir de condição