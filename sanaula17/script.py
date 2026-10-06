import chatbot

nomeChat = "Miguel,O ChupetoBot"
chatbot.saudacao(nomeChat)
while True:
    texto = chatbot.receberTexto()
    resposta = chatbot.BuscarResposta(texto)
    if chatbot.exibirResposta(nomeChat,resposta) == "End":
        break