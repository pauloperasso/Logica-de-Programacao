def calcular_pontuacao(gabarito, respostas_aluno):
    if len(gabarito) != 10 or len(respostas_aluno) != 10:
        raise ValueError("Ambas as listas devem conter exatamente 10 respostas.")

    pontuacao = 0
    for resposta_correta, resposta_aluno in zip(gabarito, respostas_aluno):
        if resposta_correta == resposta_aluno:
            pontuacao += 1

    return pontuacao

Lista_gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
Lista_respostas_aluno = ['A', 'B', 'C', 'A', 'E', 'C', 'B', 'C', 'C', 'D']
pontuacao = calcular_pontuacao(Lista_gabarito, Lista_respostas_aluno)
print(f"A pontuação do aluno é: {pontuacao} pontos.")