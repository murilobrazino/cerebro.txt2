def ensinar():
    pergunta = input("Digite a pergunta: ").strip().lower()
    resposta = input("Digite a resposta: ").strip().lower()
    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta} - {resposta}\n")
    print("bot: Aprendi!")

def conversar():
    fala = input("Você: ").strip().lower()
    encontrou = False
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    pergunta_salva, resposta_salva = dados[0], dados[1]
                    if fala == pergunta_salva:
                        print(f"bot: {resposta_salva}")
                        encontrou = True
                        break
        if not encontrou:
            print("bot: Desculpa, não sei a resposta. Use a opção 2 para me ensinar.")
    except FileNotFoundError:
        print("bot: Meu cérebro está vazio! Me ensine algo primeiro.")

def listar_conhecimento():
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("bot: Meu cérebro está vazio!")
                return
            print("\n--- O que eu já sei ---")
            for linha in linhas:
                dados = linha.strip().split(" - ")
                if len(dados) == 2:
                    print(f"Pergunta: {dados[0]} | Resposta: {dados[1]}")
            print("-----------------------\n")
    except FileNotFoundError:
        print("bot: Meu cérebro está vazio! Me ensine algo primeiro.")

while True:
    print("\n=== MENU DO CHATBOT ===")
    print("1 - Conversar")
    print("2 - Ensinar")
    print("3 - Listar conhecimento")
    print("4 - Sair")
   
    opcao = input("Escolha uma opção: ").strip()
   
    if opcao == "1":
        conversar()
    elif opcao == "2":
        ensinar()
    elif opcao == "3":
        listar_conhecimento()
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
