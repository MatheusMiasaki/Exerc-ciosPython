# Define a função para contar as repetições
def contador_repeticoes(exercicio, repeticoes):
    print("Você está fazendo", exercicio)
    print("Começando com", repeticoes, "repetições.")

    # Loop para contar as repetições
    for i in range(repeticoes):
        print("Repetição", i+1)
        input("Pressione enter para continuar")

    print("Terminou as repetições de", exercicio)

# Exemplo de uso da função
exercicio = "supino"
repeticoes = 10
contador_repeticoes(exercicio, repeticoes)

