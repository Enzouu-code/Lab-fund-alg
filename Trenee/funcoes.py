ARQ_USUARIOS = "usuarios.txt"
ARQ_VIDEOS = "videos.txt"

usuarios = []
videos = []

usuario_logado = ""


# ==========================================
# CARREGAR DADOS
# ==========================================

def carregar_dados():

    global usuarios, videos

    usuarios.clear()
    videos.clear()

    arq = open(ARQ_USUARIOS, "r", encoding="utf-8")

    for linha in arq:

        linha = linha.strip()

        if linha != "":
            usuarios.append(linha)

    arq.close()

    arq = open(ARQ_VIDEOS, "r", encoding="utf-8")

    for linha in arq:

        linha = linha.strip()

        if linha != "":
            videos.append(linha)

    arq.close()


# ==========================================
# SALVAR DADOS
# ==========================================

def salvar_dados():

    arq = open(ARQ_USUARIOS, "w", encoding="utf-8")

    for usuario in usuarios:
        arq.write(usuario + "\n")

    arq.close()

    arq = open(ARQ_VIDEOS, "w", encoding="utf-8")

    for video in videos:
        arq.write(video + "\n")

    arq.close()


# ==========================================
# USUÁRIOS
# ==========================================

def cadastrar_usuario():

    print("=== CADASTRO DE USUÁRIO ===")

    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    if login == "" or senha == "":
        print("❌ Campos inválidos.")
        return

    for usuario in usuarios:

        dados = usuario.split(";")

        if dados[0] == login:
            print("❌ Usuário já existe.")
            return

    usuarios.append(login + ";" + senha)

    salvar_dados()

    print("✅ Usuário cadastrado com sucesso.")


def fazer_login():

    global usuario_logado

    print("=== LOGIN ===")

    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    for usuario in usuarios:

        dados = usuario.split(";")

        login_salvo = dados[0]
        senha_salva = dados[1]

        if login == login_salvo and senha == senha_salva:

            usuario_logado = login

            print(f"✅ Bem-vindo, {login}!")
            return

    print("❌ Login ou senha incorretos.")


# ==========================================
# VÍDEOS
# ==========================================

def listar_videos():

    print("=== LISTA DE VÍDEOS ===")

    if len(videos) == 0:
        print("Nenhum vídeo cadastrado.")
        return

    for i, video in enumerate(videos, start=1):

        dados = video.split(";")

        nome = dados[0]
        descricao = dados[1]
        likes = dados[2]

        print(f"\n{i}. {nome}")
        print(f"Descrição: {descricao}")
        print(f"Curtidas: {likes}")


def buscar_video():

    print("=== BUSCA DE VÍDEOS ===")

    termo = input("Digite o nome do vídeo: ").strip().lower()

    encontrou = False

    for video in videos:

        dados = video.split(";")

        nome = dados[0]
        descricao = dados[1]
        likes = dados[2]

        if termo in nome.lower():

            print("\n🎬 Vídeo encontrado")
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print(f"Curtidas: {likes}")

            encontrou = True

    if not encontrou:
        print("❌ Nenhum vídeo encontrado.")


def curtir_video():

    if usuario_logado == "":
        print("❌ Faça login primeiro.")
        return

    nome = input("Nome do vídeo: ").strip().lower()

    for i in range(len(videos)):

        dados = videos[i].split(";")

        nome_video = dados[0]
        descricao = dados[1]
        likes = int(dados[2])

        if nome == nome_video.lower():

            likes += 1

            videos[i] = nome_video + ";" + descricao + ";" + str(likes)

            salvar_dados()

            print("✅ Vídeo curtido.")
            return

    print("❌ Vídeo não encontrado.")


def descurtir_video():

    if usuario_logado == "":
        print("❌ Faça login primeiro.")
        return

    nome = input("Nome do vídeo: ").strip().lower()

    for i in range(len(videos)):

        dados = videos[i].split(";")

        nome_video = dados[0]
        descricao = dados[1]
        likes = int(dados[2])

        if nome == nome_video.lower():

            if likes > 0:
                likes -= 1

            videos[i] = nome_video + ";" + descricao + ";" + str(likes)

            salvar_dados()

            print("✅ Curtida removida.")
            return

    print("❌ Vídeo não encontrado.")


# ==========================================
# PLAYLISTS
# ==========================================

def menu_playlists():

    if usuario_logado == "":
        print("❌ Faça login primeiro.")
        return

    print("=== PLAYLISTS ===")
    print("1 - Criar playlist")
    print("2 - Ver minhas playlists")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome_playlist = input("Nome da playlist: ").strip()

        if nome_playlist == "":
            print("❌ Nome inválido.")
            return

        for i in range(len(usuarios)):

            dados = usuarios[i].split(";")

            if dados[0] == usuario_logado:

                usuarios[i] += ";" + nome_playlist

                salvar_dados()

                print("✅ Playlist criada.")
                return

    elif opcao == "2":

        for usuario in usuarios:

            dados = usuario.split(";")

            if dados[0] == usuario_logado:

                print("\n=== SUAS PLAYLISTS ===")

                if len(dados) <= 2:
                    print("Nenhuma playlist criada.")
                    return

                for i in range(2, len(dados)):
                    print(f"- {dados[i]}")

                return

    else:
        print("❌ Opção inválida.")