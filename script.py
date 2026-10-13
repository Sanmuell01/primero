def inicio():
    import random
    frases = ["Bem-vindo ao Ultraquiz"
              "Boas-vindas ao ultraquiz"
              "Um novo Ultraquiz"
              "Ultraquiz!"]
    print(frases[random.randint(0,2)])

def Receber():
    texto = "P: " + input("P: ")
    return texto

def perguntar():
    with open ("base.txt", "a+")as quest:
        quest.seek(0)
        pergunta = quest.readline()
        resposta = quest.readline()
        print(pergunta)

def resposta(resposta,nome):
    print(resposta("R: ",nome))
    if resposta == "Fim":
        return "Fim"
    return "continua"