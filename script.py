perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["A) Berlim", "B) Madrid", "C) Paris", "D) Lisboa"],
        "resposta": "c",
    },
    {
        "pergunta": "resolva a equação de segundo grau x²−4x+3= 0",
        "opcoes": ["A) 1 e 2", "B)1 e 3", "C) 2 e 3", "D) 9 e 1"],
        "resposta": "b",
    },
    {
        "pergunta": "Quanto é 5 + 5?",
        "opcoes": ["A) 10", "B) 12", "C) 15", "D) 20"],
        "resposta": "a",
    },
]


print("=== ULTRAQUIZ! ===\n")

for i, p in enumerate(perguntas):
    print(f"Pergunta {i + 1}: {p['pergunta']}")
    for opcao in p["opcoes"]:
        print(opcao)

    resposta_usuario = (
        input("Escolha sua opção (A, B, C ou D): ").strip().lower()
    )

    if resposta_usuario == p["resposta"]:
        print("acertou!\n")
        
    else:
        print(f"errou")

print(
    f"Fim de jogo! Você acertou {pontuacao} de {len(perguntas)} perguntas."
)