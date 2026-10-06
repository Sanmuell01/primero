def saudacao(nome):
    import random
    frases = [
        "Eae,tudo certo?",
        "Oi",
        "oi"
        "OLá,Meu nome é " + nome + "",
        "Saudações senhor",
    ]
    return random.choice(frases)

def receberTexto():
    texto = "Cliente: " + input("Cliente: ")
    proibidas = ['feio','chupetongo','bobonauta','petista','seu feio','goybot','judeubot']
    for palavra in proibidas:
        if palavra in texto:
            print("seu feio")
            return receberTexto()
    return texto

def BuscarResposta(texto):
    with open ("base.txt", "a+") as base:
        base.seek(0)
        while True:
            linha = base.readline() random

            if linha != "":
                if texto.replace("Cliente: ","").lower() == "Tchau":
                    print("KATCHAU")
                    return "End"
                elif texto.strip().lower() == linha.strip().lower():
                    ProximaLinha = base.readline()
                    if "Chatbot: " in ProximaLinha:
                        return ProximaLinha
            else:
                print("IDK LOL")
                base.write("\n"+ texto)
                RespostaCliente = input("O que tu queria?")
                base.write("\nChatbot: " + RespostaCliente)
                return "Obrigado por esta desinformação interessante"

def exibirResposta(nomeChat,Resposta):
    if Resposta == "End":
       print("PROGRAMA ENDEDEDEDEED")
       return "End"

    print(Resposta.replace("Chatbot", nomeChat))
    return "continua"


def exibirRespostaGUI(texto, resposta, nome):
    return resposta.replace("Chatbot", nome)

def salvaSugestao(texto):
    with open("base.txt", "a+") as base:
        base.write(f"Chatbot: {texto}\n")

def buscarRespostaGUI(texto):
    with open("base.txt", "a+") as base:
        base.seek(0)
        while True:
            linha = base.readline()
            if linha != "":
                if jaccard(texto, linha) > 0.5:
                    proximaLinha = base.readline()
                    if "Chatbot:" in proximaLinha:
                        return proximaLinha
            else:
                base.write("\n" + texto)
                return "não sei"


def jaccard(msg, base):
    msg = limparFrase(msg)
    base = limparFrase(base)

    if len(base) < 1:
        return 0
    else:
        palavrasComum = 0
        for palavra in msg.split():
            if palavra in base.split():
                palavrasComum += 1
        return palavrasComum / len(base.split())

def limparFrase(texto):
    tirar = ["?", "!", "...", ".", ",", "Cliente: ", "\n"]
    for op in tirar:
        texto = texto.replace(op, "")
    return texto.upper()

