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
# FAVORITOS
# =====================================

def ver_favoritos():

    if usuario_logado == "":
        print("❌ Login necessário")
        return

    for u in usuarios:

        dados = u.split(";")

        if dados[0] == usuario_logado:

            print("\n=== FAVORITOS ===")

            if len(dados) < 3 or dados[2] == "":
                print("Nenhum favorito")
                return

            favoritos = dados[2].split(",")

            for f in favoritos:
                print("❤️", f)

            return


def adicionar_favorito():

    if usuario_logado == "":
        print("❌ Login necessário")
        return

    nome_video = input("Vídeo para favoritar: ")

    video_existe = False

    for v in videos:

        dados_video = v.split(";")

        if nome_video.lower() == dados_video[0].lower():
            video_existe = True
            break

    if not video_existe:
        print("❌ Vídeo não encontrado")
        return

    for i in range(len(usuarios)):

        dados = usuarios[i].split(";")

        if dados[0] == usuario_logado:

            favoritos = []

            if len(dados) >= 3 and dados[2] != "":
                favoritos = dados[2].split(",")

            if nome_video in favoritos:
                print("❌ Já favoritado")
                return

            favoritos.append(nome_video)

            if len(dados) >= 3:
                dados[2] = ",".join(favoritos)
            else:
                dados.append(",".join(favoritos))

            usuarios[i] = ";".join(dados)

            salvar_dados()

            print("✅ Favoritado")
            return

    print("❌ Usuário não encontrado")


def remover_favorito():

    if usuario_logado == "":
        print("❌ Login necessário")
        return

    nome_video = input("Vídeo para remover: ")

    for i in range(len(usuarios)):

        dados = usuarios[i].split(";")

        if dados[0] == usuario_logado:

            if len(dados) < 3 or dados[2] == "":
                print("❌ Nenhum favorito")
                return

            favoritos = dados[2].split(",")

            if nome_video not in favoritos:
                print("❌ Vídeo não favoritado")
                return

            favoritos.remove(nome_video)

            dados[2] = ",".join(favoritos)

            usuarios[i] = ";".join(dados)

            salvar_dados()

            print("✅ Removido dos favoritos")
            return

    print("❌ Usuário não encontrado")

