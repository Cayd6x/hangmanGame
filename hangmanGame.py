import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'forca', 'computador', 'teclado']
    return random.choice(palavras)

def mostrar_tabuleiro(palavra, letras_acertadas):
    print("\nPalavra: ", end="")
    for letra in palavra:
        if letra in letras_acertadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")

def obter_palpite():
    return input("Adivinhe uma letra: ").lower()

def jogar_novamente():
    return input("Deseja jogar novamente? (s/n): ").lower().startswith('s')

def desenhar_forca(erros):
    estagios = ["""
                   --------
                   |      |
                   |      
                   |    
                   |    
                   |    
                --------
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |    
                   |    
                --------
                """,
                # Mais estagios aqui
                ]
    print(estagios[erros])

def jogo_da_forca():
    palavra_oculta = escolher_palavra()
    letras_acertadas = []
    erros = 0

    while True:
        mostrar_tabuleiro(palavra_oculta, letras_acertadas)
        palpite = obter_palpite()

        if palpite in palavra_oculta and palpite not in letras_acertadas:
            letras_acertadas.append(palpite
