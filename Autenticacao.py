senha = '102030'
while True:

    entrada = input("[E]Entrar\n[S]Sair\nEscolha uma opção: ").strip().upper()

    if not entrada:
        print('Opção inválida. Digite algo.\n')

    if entrada == 'E':
        print('Entrando...\n')

        while True:
            senha_digitada = input("Digite a senha: ")

            if senha_digitada == senha:
                print("Acesso permitido!\n")
                break
            else:
                print("Senha incorreta. Tente novamente.\n")

    elif entrada == 'S':
        print('Saindo...\n')
        break