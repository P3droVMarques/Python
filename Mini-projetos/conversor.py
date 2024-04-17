unidade = input("Qual unidade vc deseja converter? ")
Cm = int(input("Digite o valor: "))
M = Cm/100
Km = Cm/100000

if unidade == "Km":
 print("O valor em quilometros será de:", Km)
  
if unidade == "M":
 print("O valor em metros será de:", M)

if unidade == "Cm":
 print("O valor em centimetros será de:", Cm)

else:
 print("erro")