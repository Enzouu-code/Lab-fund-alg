import json
import os

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_VIDEOS   = "videos.json"

usuarios = {}
videos = {}
usuario_logado = None


import json
import os

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_VIDEOS   = "videos.json"

usuarios = {}
videos = {}
usuario_logado = None


# ── PERSISTÊNCIA ─────────────────────────────────────────

def carregar_dados():
    global usuarios, videos

    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            usuarios = json.load(f)

    if os.path.exists(ARQUIVO_VIDEOS):
        with open(ARQUIVO_VIDEOS, "r", encoding="utf-8") as f:
            videos = json.load(f)


def salvar_dados():
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=2, ensure_ascii=False)

    with open(ARQUIVO_VIDEOS, "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=2, ensure_ascii=False)


# ── HELPERS ──────────────────────────────────────────────

def requer_login():
    if usuario_logado is None:
        print("Faça login primeiro.")
        return False
    return True


def exibir_video(nome):
    v = videos[nome]
    print(f"\n🎬 {nome}")
    print(f"Descrição: {v['descricao']}")
    print(f"Gênero: {v.get('genero', '-')}")
    print(f"Ano: {v.get('ano', '-')}")
    print(f"Likes: {v['likes']}")


def get_usuario():
    return usuarios[usuario_logado]


# ── USUÁRIOS ─────────────────────────────────────────────

def cadastrar_usuario():
    login = input("Login: ")

    if not login:
        print("Login vazio.")
        return

    if login in usuarios:
        print("Já existe.")
        return

    senha = input("Senha: ")

    usuarios[login] = {
        "senha": senha,
        "curtidos": [],
        "playlists": {}
    }

    salvar_dados()
    print("Usuário criado!")


def fazer_login():
    global usuario_logado

    if usuario_logado:
        print("Já está logado.")
        return

    login = input("Login: ")
    senha = input("Senha: ")

    if login not in usuarios:
        print("Usuário não existe.")
        return

    if usuarios[login]["senha"] == senha:
        usuario_logado = login
        print("Logado!")
    else:
        print("Senha errada.")


def fazer_logout():
    global usuario_logado
    usuario_logado = None
    print("Logout feito.")


# ── VÍDEOS ───────────────────────────────────────────────

def cadastrar_video():
    if not requer_login():
        return

    nome = input("Nome: ")

    if nome in videos:
        print("Já existe.")
        return

    videos[nome] = {
        "descricao": input("Descrição: "),
        "genero": input("Gênero: "),
        "ano": input("Ano: "),
        "likes": 0
    }

    salvar_dados()
    print("Vídeo cadastrado!")


def listar_videos():
    if not videos:
        print("Nenhum vídeo.")
        return

    for nome in videos:
        exibir_video(nome)


def buscar_video():
    termo = input("Buscar: ").lower()

    encontrados = [n for n in videos if termo in n.lower()]

    for nome in encontrados:
        exibir_video(nome)


def curtir_video():
    if not requer_login():
        return

    nome = input("Vídeo: ")

    if nome not in videos:
        print("Não existe.")
        return

    user = get_usuario()

    if nome in user["curtidos"]:
        print("Já curtiu.")
        return

    user["curtidos"].append(nome)
    videos[nome]["likes"] += 1

    salvar_dados()
    print("Curtiu!")


def descurtir_video():
    if not requer_login():
        return

    nome = input("Vídeo: ")
    user = get_usuario()

    if nome not in user["curtidos"]:
        print("Você não curtiu.")
        return

    user["curtidos"].remove(nome)
    videos[nome]["likes"] -= 1

    salvar_dados()
    print("Descurtiu.")


# ── PLAYLISTS ────────────────────────────────────────────

def menu_playlists():
    if not requer_login():
        return

    while True:
        print("\n1 Criar")
        print("2 Listar")
        print("3 Adicionar vídeo")
        print("4 Ver playlist")
        print("0 Voltar")

        op = input("Opção: ")
        playlists = get_usuario()["playlists"]

        if op == "1":
            nome = input("Nome: ")
            playlists[nome] = []
            salvar_dados()

        elif op == "2":
            for p in playlists:
                print(p)

        elif op == "3":
            pl = input("Playlist: ")
            vid = input("Vídeo: ")

            if pl in playlists and vid in videos:
                playlists[pl].append(vid)
                salvar_dados()

        elif op == "4":
            pl = input("Playlist: ")
            for vid in playlists.get(pl, []):
                exibir_video(vid)

        elif op == "0":
            break