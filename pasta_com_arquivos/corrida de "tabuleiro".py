import random
import time

mensagens = {
    "pt": {
        "menu": "Escolha uma opção:\n iniciar \n configurações \n créditos",
        "digit_nome": "Digite o nome do jogador: ",
        "nenhum_jogador": "Nenhum jogador cadastrado. Saindo...",
        "sua_vez": "sua vez! (pressione ENTER para rolar o dado)",
        "rolando": "Rolando o dado...",
        "saiu": "Saiu o número",
        "vencedor": "você venceu!!!! Parabéns!!!!",
        "placar": "--- Placar ---",
        "lider": "Líder(es):",
        "idioma": "Escolha o idioma:\n1 - Português\n2 - English\n3 - Español",
        "msg_esc": "Opção inválida. Mantendo Português.",
        "tempo": "Escolha o tempo de rolagem do dado (em segundos, ex: 1.5): ",
        "carta": "Carta sorteada"
    },
    "en": {
        "menu": "Choose an option:\n start \n settings \n credits",
        "digit_nome": "Enter player's name: ",
        "nenhum_jogador": "No players registered. Exiting...",
        "sua_vez": "your turn! (press ENTER to roll the dice)",
        "rolando": "Rolling the dice...",
        "saiu": "Rolled the number",
        "vencedor": "you won!!!! Congratulations!!!!",
        "placar": "--- Score ---",
        "lider": "Leader(s):",
        "idioma": "Choose the language:\n1 - Português\n2 - English\n3 - Español",
        "msg_esc": "Invalid option. Keeping English.",
        "tempo": "Choose dice rolling time (seconds, e.g., 1.5): ",
        "carta": "Drawn card"
    },
    "es": {
        "menu": "Elija una opción:\n iniciar \n configuraciones \n créditos",
        "digit_nome": "Ingrese el nombre del jugador: ",
        "nenhum_jogador": "No hay jugadores registrados. Saliendo...",
        "sua_vez": "¡tu turno! (presione ENTER para tirar el dado)",
        "rolando": "Tirando el dado...",
        "saiu": "Número obtenido",
        "vencedor": "¡has ganado!!!! Felicidades!!!!",
        "placar": "--- Puntuación ---",
        "lider": "Líder(es):",
        "idioma": "Elige el idioma:\n1 - Português\n2 - English\n3 - Español",
        "msg_esc": "Opción inválida. Se mantiene Español.",
        "tempo": "Elige el tiempo de lanzamiento del dado (segundos, ej: 1.5): ",
        "carta": "Carta sorteada"
    }
}

lang = "pt"
tempo_dado = 1.5

cartas_dict = {
    "pt": [
        "Avança 2", "Avança 5", "Recua 2", "Recua 5", "Troca de Posição", "Dado Duplo",
        "Dado Zero", "Sorte Grande", "Azar", "Reroll", "Pare!", "Barreira", "Escudo",
        "Inversão", "Congela Turno", "Bônus de Chegada", "Troca de Pontos",
        "Velocidade", "Sorteio de Carta", "Carta Secreta"
    ],
    "en": [
        "Advance 2", "Advance 5", "Go Back 2", "Go Back 5", "Swap Position", "Double Dice",
        "Zero Dice", "Big Luck", "Bad Luck", "Reroll", "Stop!", "Barrier", "Shield",
        "Inversion", "Freeze Turn", "Finish Bonus", "Swap Points",
        "Speed", "Draw Card", "Secret Card"
    ],
    "es": [
        "Avanza 2", "Avanza 5", "Retrocede 2", "Retrocede 5", "Intercambio de Posición", "Dado Doble",
        "Dado Cero", "Buena Suerte", "Mala Suerte", "Rehacer", "¡Alto!", "Barrera", "Escudo",
        "Inversión", "Congelar Turno", "Bono de Llegada", "Intercambiar Puntos",
        "Velocidad", "Sorteo de Carta", "Carta Secreta"
    ]
}

def menu():
    print(mensagens[lang]["menu"])
    opcao = str(input(""))
    return opcao.lower()

def configuracoes():
    global lang, tempo_dado
    print(mensagens[lang]["idioma"])
    escolha = input("")
    if escolha == "1":
        lang = "pt"
    elif escolha == "2":
        lang = "en"
    elif escolha == "3":
        lang = "es"
    else:
        print(mensagens[lang]["msg_esc"])
    try:
        tempo_dado = float(input(mensagens[lang]["tempo"]))
    except:
        print("Valor inválido. Mantendo padrão.")

def corrida():
    players = []
    while len(players) < 5:
        x = str(input(mensagens[lang]["digit_nome"]))
        if x == '':
            break
        players.append(x)
    if len(players) == 0:
        print(mensagens[lang]["nenhum_jogador"])
        return

    pontos = [0] * len(players)
    skip_turn = [False] * len(players)
    vencedor = False
    turno = 0

    while not vencedor:
        jogador_atual = players[turno]
        if skip_turn[turno]:
            print(f"{jogador_atual} perdeu a vez!")
            skip_turn[turno] = False
            turno = (turno + 1) % len(players)
            continue
        print(f"\n{jogador_atual}, {mensagens[lang]['sua_vez']}")
        input("")
        print(mensagens[lang]["rolando"])
        time.sleep(tempo_dado)
        dado = random.randint(1, 6)
        print(f"{mensagens[lang]['saiu']} {dado}!")

        cartas = cartas_dict[lang]
        carta_sorteada = random.choice(cartas)
        print(f"{mensagens[lang]['carta']}: {carta_sorteada}")

        if "Avança" in carta_sorteada or "Advance" in carta_sorteada or "Avanza" in carta_sorteada:
            pontos[turno] += 2 + dado
        elif "Recua" in carta_sorteada or "Go Back" in carta_sorteada or "Retrocede" in carta_sorteada:
            pontos[turno] -= 2
            pontos[turno] += dado
        elif "Dado Duplo" in carta_sorteada or "Double Dice" in carta_sorteada or "Dado Doble" in carta_sorteada:
            dado2 = random.randint(1, 6)
            pontos[turno] += dado + dado2
        elif "Dado Zero" in carta_sorteada or "Zero Dice" in carta_sorteada or "Dado Cero" in carta_sorteada:
            pontos[turno] += 0
        elif "Sorte Grande" in carta_sorteada or "Big Luck" in carta_sorteada or "Buena Suerte" in carta_sorteada:
            bonus = random.randint(1, 6)
            pontos[turno] += dado + bonus
        elif "Azar" in carta_sorteada or "Bad Luck" in carta_sorteada or "Mala Suerte" in carta_sorteada:
            malus = random.randint(1, 6)
            pontos[turno] += dado - malus
        elif "Reroll" in carta_sorteada or "Rehacer" in carta_sorteada:
            dado2 = random.randint(1, 6)
            pontos[turno] += dado2
        elif "Pare" in carta_sorteada or "Stop" in carta_sorteada or "¡Alto" in carta_sorteada:
            outros = [i for i in range(len(players)) if i != turno]
            alvo = random.choice(outros)
            skip_turn[alvo] = True
            pontos[turno] += dado
        elif "Troca de Posição" in carta_sorteada or "Swap Position" in carta_sorteada or "Intercambio de Posición" in carta_sorteada:
            outros = [i for i in range(len(players)) if i != turno]
            alvo = random.choice(outros)
            pontos[turno], pontos[alvo] = pontos[alvo], pontos[turno]
            pontos[turno] += dado
        elif "Escudo" in carta_sorteada or "Shield" in carta_sorteada:
            pontos[turno] += dado
        elif "Inversão" in carta_sorteada or "Inversion" in carta_sorteada or "Inversión" in carta_sorteada:
            frente = max(range(len(players)), key=lambda i: pontos[i] if i != turno else -1)
            pontos[frente] -= dado
            pontos[turno] += dado
        elif "Congela Turno" in carta_sorteada or "Freeze Turn" in carta_sorteada or "Congelar Turno" in carta_sorteada:
            outros = [i for i in range(len(players)) if i != turno]
            alvo = random.choice(outros)
            skip_turn[alvo] = True
            pontos[turno] += dado
        elif "Bônus de Chegada" in carta_sorteada or "Finish Bonus" in carta_sorteada or "Bono de Llegada" in carta_sorteada:
            if pontos[turno] >= 45:
                pontos[turno] = 50
            else:
                pontos[turno] += dado
        elif "Troca de Pontos" in carta_sorteada or "Swap Points" in carta_sorteada or "Intercambiar Puntos" in carta_sorteada:
            outros = [i for i in range(len(players)) if i != turno]
            alvo = random.choice(outros)
            pontos[turno], pontos[alvo] = pontos[alvo], pontos[turno]
            pontos[turno] += dado
        elif "Velocidade" in carta_sorteada or "Speed" in carta_sorteada or "Velocidad" in carta_sorteada:
            pontos[turno] += dado
            print(f"{players[turno]} joga novamente!")
            continue
        elif "Sorteio de Carta" in carta_sorteada or "Draw Card" in carta_sorteada or "Sorteo de Carta" in carta_sorteada:
            carta_extra = random.choice(cartas)
            print(f"Carta extra sorteada: {carta_extra}")
            pontos[turno] += dado
        elif "Carta Secreta" in carta_sorteada or "Secret Card" in carta_sorteada or "Carta Secreta" in carta_sorteada:
            if pontos[turno] >= 40:
                bonus = random.randint(1, 6)
                print(f"Carta secreta revela: +{bonus} pontos!")
                pontos[turno] += dado + bonus
            else:
                pontos[turno] += dado
        else:
            pontos[turno] += dado

        if pontos[turno] >= 50:
            print(f"\n{jogador_atual} {mensagens[lang]['vencedor']}")
            vencedor = True
            break

        print("\n" + mensagens[lang]["placar"])
        for i, p in enumerate(players):
            print(f"{p}: {pontos[i]} pontos")
        max_pontos = max(pontos)
        lideres = [players[i] for i, p in enumerate(pontos) if p == max_pontos]
        print(mensagens[lang]["lider"], ", ".join(lideres))
        turno = (turno + 1) % len(players)

if __name__ == '__main__':
    while True:
        op = menu()
        if op in ['iniciar','start','iniciar']:
            corrida()
        elif op in ['configurações','settings','configuraciones']:
            configuracoes()
        elif op in ['créditos','credits','créditos']:
            print("\nJogo desenvolvido em Python. Divirta-se!")
        else:
            print("Opção inválida.")
