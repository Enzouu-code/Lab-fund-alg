import funcoes
import os
import time

def limpar():
    os.system("cls")


funcoes.carregar_dados()

while True:
    logado_info = f" [{funcoes.usuario_logado}]" if funcoes.usuario_logado else " [não logado]"

    print(f"\n{'═'*40}")
    print(f"        🎬 FEItv{logado_info}")
    print(f"{'═'*40}")
    print("1  - Cadastrar usuário")
    print("2  - Login")
    print("─" * 40)
    print("3  - Buscar vídeo por nome")
    print("4  - Listar vídeos")
    print("─" * 40)
    print("5  - Curtir vídeo")
    print("6  - Descurtir vídeo")
    print("─" * 40)
    print("7  - Gerenciar playlists")
    print("─" * 40)
    print("0  - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    limpar()

    if opcao == "1":
        funcoes.cadastrar_usuario()
        time.sleep(1)

    elif opcao == "2":
        funcoes.fazer_login()
        time.sleep(1)

    elif opcao == "3":
        funcoes.buscar_video()
        time.sleep(2)

    elif opcao == "4":
        funcoes.listar_videos()
        time.sleep(2)

    elif opcao == "5":
        funcoes.curtir_video()
        time.sleep(1)

    elif opcao == "6":
        funcoes.descurtir_video()
        time.sleep(1)

    elif opcao == "7":
        funcoes.menu_playlists()
        time.sleep(1)

    elif opcao == "0":
        funcoes.salvar_dados()
        print("Saindo...")
        time.sleep(1)
        break

    else:
        print("Opção inválida.")
        time.sleep(1)
