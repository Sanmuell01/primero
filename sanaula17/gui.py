from tkinter import *
import chatbot as c

tela = Tk()
tela.title("Miguel,O ChupetoBot")
tela.geometry("1080x1920")
tela.grid()

frame1 = Frame(tela)
frame1.grid()

instrucao = Label(frame1, text="Insira mensagem: ")
instrucao.grid(row=0,column=0)

entradaMsg = Entry(frame1)
entradaMsg.grid(row=0,column=1)

frame2 = Frame(tela)
frame2.grid(row=1,column=0)

v = StringVar()
Label(frame2, textvariable=v).grid()



nomeChat = "MiguelBot,O chupetoBot"
v.set("Say Your name: ")
entradaSug = False
NSNome = True
nome = ""

def RodaChatBot():
    global entradaSug
    global NSNome
    global nome
    global historico
    if NSNome:
        NSNome = entradaMsg.get()
        saudacao = c.saudacao(nomeChat)
        historico = f"{nomeChat}: ^{saudacao}\n"
        v.set(historico)
        NSNome = False
    else:
        texto = entradaMsg.get()
        historico += "\n" + nome + ": " + texto
        v.set(historico)

        if entradaSug:
            c.salvaSugestao(texto)
            entradaSug = False
            historico += "\n Aprendi meu povo,vamo estorquir o Brasil!.\n"
            v.set(historico)
        else:
            resposta = c.buscarRespostaGUI("Cliente: " + texto + "\n")
            if "não sei" in resposta:
                historico += "\nNão sei,o que desejas\n"
                v.set(historico)
                entradaSug = True
            else:
                historico += "\n" + c.exibirRespostaGUI(texto, resposta, nomeChat)
                v.set(historico)
 
Button(frame1, text="Enviar",command=RodaChatBot).grid(row=0,column=2)

    
tela.mainloop()