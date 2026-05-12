import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARQ_USUARIOS = os.path.join(BASE_DIR, "usuarios.txt")
ARQ_VIDEOS = os.path.join(BASE_DIR, "videos.txt")

usuarios = []
videos = []

usuario_logado = ""


# =====================================
# CARREGAR DADOS
# =====================================

def carregar_dados():

    global usuarios, videos

    usuarios.clear()
    videos.clear()

    if not os.path.exists(ARQ_USUARIOS):
        open(ARQ_USUARIOS, "w").close()

    if not os.path.exists(ARQ_VIDEOS):
        open(ARQ_VIDEOS, "w").close()

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


# =====================================
# SALVAR DADOS
# =====================================

def salvar_dados():

    arq = open(ARQ_USUARIOS, "w", encoding="utf-8")

    for u in usuarios:
        arq.write(u + "\n")

    arq.close()

    arq = open(ARQ_VIDEOS, "w", encoding="utf-8")

    for v in videos:
        arq.write(v + "\n")

    arq.close()


# =====================================
# USUÁRIOS
# =====================================

def cadastrar_usuario():

    print("=== CADASTRO ===")

    login = input("Login: ")
    senha = input("Senha: ")

    if login == "" or senha == "":
        print("❌ Inválido")
        return

    for u in usuarios:

        dados = u.split(";")

        if dados[0] == login:
            print("❌ Já existe")
            return

    usuarios.append(login + ";" + senha)

    salvar_dados()

    print("✅ Criado")


def fazer_login():

    global usuario_logado

    print("=== LOGIN ===")

    login = input("Login: ")
    senha = input("Senha: ")

    for u in usuarios:

        dados = u.split(";")

        if login == dados[0] and senha == dados[1]:

            usuario_logado = login

            print("✅ Logado")
            return

    print("❌ Erro")


# =====================================
# VÍDEOS
# =====================================

def listar_videos():

    print("=== VÍDEOS ===")

    if len(videos) == 0:
        print("Nenhum vídeo")
        return

    for v in videos:

        dados = v.split(";")

        print("\nNome:", dados[0])
        print("Descrição:", dados[1])
        print("Likes:", dados[2])


def buscar_video():

    termo = input("Buscar: ")

    for v in videos:

        dados = v.split(";")

        if termo.lower() in dados[0].lower():

            print("\nEncontrado")
            print("Nome:", dados[0])
            print("Descrição:", dados[1])
            print("Likes:", dados[2])
            return

    print("❌ Não encontrado")


def curtir_video():

    if usuario_logado == "":
        print("❌ Login necessário")
        return

    nome = input("Vídeo: ")

    for i in range(len(videos)):

        dados = videos[i].split(";")

        if nome.lower() == dados[0].lower():

            likes = int(dados[2]) + 1

            videos[i] = dados[0] + ";" + dados[1] + ";" + str(likes)

            salvar_dados()

            print("❤️ Curtido")
            return

    print("❌ Não achado")


def descurtir_video():

    if usuario_logado == "":
        print("❌ Login necessário")
        return

    nome = input("Vídeo: ")

    for i in range(len(videos)):

        dados = videos[i].split(";")

        if nome.lower() == dados[0].lower():

            likes = int(dados[2])

            if likes > 0:
                likes = likes - 1

            videos[i] = dados[0] + ";" + dados[1] + ";" + str(likes)

            salvar_dados()

            print("💔 Removido")
            return

    print("❌ Não achado")


# =====================================
# PLAYLISTS
# =====================================

def menu_playlists():

    if usuario_logado == "":
        print("❌ Login necessário")
        return

    print("1 - Criar")
    print("2 - Ver")

    op = input("Opção: ")

    for i in range(len(usuarios)):

        dados = usuarios[i].split(";")

        if dados[0] == usuario_logado:

            if op == "1":

                nome = input("Nome playlist: ")

                usuarios[i] = usuarios[i] + ";" + nome

                salvar_dados()

                print("✅ Criada")
                return

            elif op == "2":

                if len(dados) <= 2:
                    print("Sem playlists")
                    return

                print("\n=== PLAYLISTS ===")

                for j in range(2, len(dados)):
                    print("-", dados[j])

                return

            else:
                print("❌ Opção inválida")
                return