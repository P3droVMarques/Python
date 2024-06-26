#Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância
#do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave: valor separada por vírgulas.

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

#Acesso aos dados#

#Os dados são acessados e modificados através da chave.

dados =  {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # "Guilherme"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

#Dicionário aninhados#

#Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto
#imutável como (strings e números).

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"] #|3443-2121

#Iterar dicionários

#A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for.

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

#"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
#"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
#"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}
#"melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"}

#Métodos da classe dict#

#{}.clear

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"},
}

contatos.clear() 
 #{}

#{}.copy

contato = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"]

copia["guilherme@gmail.com"]

#{}.fromkeys

dict.fromkeys(["nome", "telefone"]) #{"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

#{}.get

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos["chave"]

contatos.get("chave") #None
contatos.get("chave", {}) #{}
contatos.get("guilherme@gmail.com", {}) #{"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

#{}.items

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.items() #dict_items([("guilherme@gmail.com",{"nome": "Guilherme", "telefone": "3333-2221"})])

#{}.keys

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.keys() # dict_keys(["guilherme@gmail.com"])

#{}.pop

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.pop("guilherme@gmail.com") #{"nome": "Guilherme", "telefone": "3333-2221"}
contatos.pop("guilherme@gmail.com", {}) #{}

#{}.popitem

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.popitem("guilherme@gmail.com") #("guilherme@gmail.com", {"nome": "Guilherme", "telefone": "3333-2221"})
contatos.popitem("guilherme@gmail.com", {}) # KeyError

#{}.setdefault

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna") # "Guilherme" 
contato # {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("idade", 28) # 28
contato # {"nome": "Guilherme", "telefone": "3333-2221", "idade": 28}

#{}.update

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {"guilherme@gmail.com": {"nome":"Gui"}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos # {"guilherme@gmail.com": {"nome": "Gui"}, "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}

#{}.values

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

contatos.values() # dict_values([{"nome": "Guilherme", "telefone": "3333-2221"}, {"nome": "Giovanna", "telefone": "3443-2121"}, {"nome": "Chappie", "telefone": "3344-9871"}, {"nome": "Melaine", "telefone": "3333-7766"}])

#in

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

"guilherme@gmail.com" in contatos #True
"megui@gmail.com" in contatos #False
"idade" in contatos["guilherme@gmail.com"] #False
"telefone" in contatos["giovanna@gmail.com"] #True

#del

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

contatos # {"guilherme@gmail.com": {"nome": "Guilherme"}, "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}, "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}  }