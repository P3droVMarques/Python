while True:
    num1 = int(input("Digite o primeiro número: "))
    operacao = input('Qual a operação que será realizada? ')
    num2 = int(input("Digite o segundo número: "))
    

    # Adicao
    if operacao == "+":
     print('{} + {} = '.format(num1, num2))
     print(num1 + num2)
     
    # Subtracao
    elif operacao == '-':
     print('{} - {} = '.format(num1, num2))
     print(num1 - num2)

    # Multiplicacão
    elif operacao == "*":
     print('{} * {} = '.format(num1, num2))
     print(num1 * num2)

    # Divisao
    elif operacao == "/":
     print('{} / {} = '.format(num1, num2))
     print(num1 / num2)

    else: print("operador inválido")

    msg = input("Deseja continuar? (S/N): ") 
    
    if msg != "S":
      print("Obrigado por utilizar a calculadora")
      break