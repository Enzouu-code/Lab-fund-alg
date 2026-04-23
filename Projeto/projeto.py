
senhas = []
logins = []
videos = []
descri = []
likes = []




def cadastrar_usuario():
    login = input("Login: ")

    if login in logins:
        print("login já existe!")
        return
    
    senha = input("Senha: ")

    logins.append(login)
    senhas.append(senha)
    print("Usuário cadastrado com sucesso!")


def fazer_login():
    login = input("Login: ")
    senha = input("Senha: ")

    if login not in logins:
        print("Usuário não encontrado")
        return
    
    indice = logins.index(login)

    if senhas[indice] == senha:
        print("Login realizado com Sucesso")
    else:
        print("Senha incorreta")

def buscar_nome():
    nome = input("Digite o nome do vídeo: ")

    if nome in videos:
        indice = videos.index(nome)

        print("\n--- Vídeo encontrado ---")
        print(f"Nome: {videos[indice]}")
        print(f"Descrição: {descri[indice]}")
        print(f"Likes: {likes[indice]}")
    else:
        print("Vídeo não encontrado")

def curtir_video():
    nome = input("Qual vídeo deseja curtir? ")

    if nome in videos:
        indice = videos.index(nome)
        likes[indice] += 1
        print("Curtido!")
    else:
        print("Vídeo não encontrado!")


def descurtir_video():
    nome = input("Qual vídeo deseja descurtir? ")

    if nome in videos:
        indice = videos.index(nome)

        if likes[indice] > 0:
            likes[indice] -= 1

        print("Descurtido!")
    else:
        print("Vídeo não encontrado!")



while True:
    print("\n----MENU----")
    print("\n1- Cadastrar Usuário")
    print("2- Fazer Login")
    print("3- Curtir")
    print("4- Descurtir vídeos")
    print("5- Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        logado = fazer_login()

        if logado:
            print("Bem-Vindo à Plataforma!")
    
    elif opcao == "3":
        curtir_video()

    elif opcao == "4":
        descurtir_video()

    elif opcao == "5":
        print("Saindo...")

    else:
        print("Opção Inválida")



