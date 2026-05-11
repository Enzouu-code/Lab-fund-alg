ARQ_USUARIOS = "usuarios.txt"
ARQ_VIDEOS = "videos.txt"

usuarios = []
videos = []

usuario_logado = ""


# ─────────────────────────────
# CARREGAR
# ─────────────────────────────

def carregar_dados():
    global usuarios, videos

    usuarios.clear()
    videos.clear()

    arq = open(ARQ_USUARIOS, "r", encoding="utf-8")

    for linha in arq:
        usuarios.append(linha.strip())

    arq.close()

    arq = open(ARQ_VIDEOS, "r", encoding="utf-8")

    for linha in arq:
        videos.append(linha.strip())

    arq.close()


# ─────────────────────────────
# SALVAR
# ─────────────────────────────

def salvar_dados():
    arq = open(ARQ_USUARIOS, "w", encoding="utf-8")

    for usuario in usuarios:
        arq.write(usuario + "\n")

    arq.close()

    arq = open(ARQ_VIDEOS, "w", encoding="utf-8")

    for video in videos:
        arq.write(video + "\n")

    arq.close()


# ─────────────────────────────
# USUÁRIO
# ─────────────────────────────

def cadastrar_usuario():
    login = input("Login: ")
    senha = input("Senha: ")

    usuarios.append(login + ";" + senha)

    salvar_dados()
    print("Usuário criado.")


def fazer_login():
    global usuario_logado

    login = input("Login: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        dados = usuario.split(";")

        login_salvo = dados[0]
        senha_salva = dados[1]

        if login == login_salvo and senha == senha_salva:
            usuario_logado = login
            print("Logado!")
            return

    print("Erro no login.")


# ─────────────────────────────
# VÍDEOS
# ─────────────────────────────

def listar_videos():
    if len(videos) == 0:
        print("Nenhum vídeo.")
        return

    for video in videos:
        dados = video.split(";")

        print(dados[0] + " - " + dados[1] + " - likes: " + dados[2])


def buscar_video():
    termo = input("Buscar: ").strip().lower()

    achou = 0

    for video in videos:
        dados = video.split(";")

        nome = dados[0].strip().lower()
        descricao = dados[1]

        if termo in nome:
            print(dados[0] + " - " + descricao)
            achou = 1

    if achou == 0:
        print("Nada encontrado.")


def curtir_video():
    if usuario_logado == "":
        print("Faça login.")
        return

    nome = input("Vídeo: ").strip()

    i = 0

    while i < len(videos):
        dados = videos[i].split(";")

        nome_video = dados[0]
        descricao = dados[1]
        likes = int(dados[2])

        if nome_video == nome:
            likes = likes + 1
            videos[i] = nome_video + ";" + descricao + ";" + str(likes)

            salvar_dados()
            print("Curtido.")
            return

        i = i + 1

    print("Vídeo não encontrado.")


def descurtir_video():
    if usuario_logado == "":
        print("Faça login.")
        return

    nome = input("Vídeo: ").strip()

    i = 0

    while i < len(videos):
        dados = videos[i].split(";")

        nome_video = dados[0]
        descricao = dados[1]
        likes = int(dados[2])

        if nome_video == nome:
            if likes > 0:
                likes = likes - 1

            videos[i] = nome_video + ";" + descricao + ";" + str(likes)

            salvar_dados()
            print("Removido.")
            return

        i = i + 1

    print("Vídeo não encontrado.")


# ─────────────────────────────
# PLAYLIST (SIMPLES)
# ─────────────────────────────

def menu_playlists():
    if usuario_logado == "":
        print("Faça login.")
        return

    print("\n1 - Criar playlist")
    print("2 - Ver dados do usuário")

    op = input("Opção: ")

    if op == "1":
        nome_playlist = input("Nome da playlist: ")

        for i in range(len(usuarios)):
            dados = usuarios[i].split(";")

            if dados[0] == usuario_logado:
                usuarios[i] = usuarios[i] + ";" + nome_playlist
                salvar_dados()
                print("Playlist criada.")

    elif op == "2":
        for usuario in usuarios:
            if usuario.startswith(usuario_logado):
                print(usuario)
