import funcoes

def menu_principal():
    while True:
        logado_info = f" [{funcoes.usuario_logado}]" if funcoes.usuario_logado else " [não logado]"
        
        print(f"\n{'═'*40}")
        print(f"        🎬  FEItv{logado_info}")
        print(f"{'═'*40}")
        print("1  - Cadastrar usuário")
        print("2  - Login")
        print("3  - Logout")
        print("─" * 40)
        print("4  - Cadastrar vídeo")
        print("5  - Buscar vídeo por nome")
        print("6  - Listar todos os vídeos")
        print("─" * 40)
        print("7  - Curtir vídeo")
        print("8  - Descurtir vídeo")
        print("─" * 40)
        print("9  - Gerenciar playlists (favoritos)")
        print("─" * 40)
        print("0  - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if   opcao == "1": funcoes.cadastrar_usuario()
        elif opcao == "2": funcoes.fazer_login()
        elif opcao == "3": funcoes.fazer_logout()
        elif opcao == "4": funcoes.cadastrar_video()
        elif opcao == "5": funcoes.buscar_video()
        elif opcao == "6": funcoes.listar_videos()
        elif opcao == "7": funcoes.curtir_video()
        elif opcao == "8": funcoes.descurtir_video()
        elif opcao == "9": funcoes.menu_playlists()
        elif opcao == "0":
            funcoes.salvar_dados()
            print("💾 Dados salvos. Até logo!")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    funcoes.carregar_dados()
    menu_principal()