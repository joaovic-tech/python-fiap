"""
TODO: Adicionar while na estrutura para perguntar ao usuário se deseja sair.
"""

NIVEL_ADM = "ADM"
NIVEL_USR = "USR"
NIVEL_GUEST = "GUEST"
GENERO_M = "MASCULINO"
GENERO_F = "FEMININO"

continuar = True

while continuar != "SIM":
    continuar = input("Digite SIM para sair: ").upper()

    if continuar == "SIM":
        break

    acesso = input("Digite o seu nível de acesso (ADM, USR ou GUEST): ").strip().upper()

    if acesso == NIVEL_ADM or acesso == NIVEL_USR:
        genero = input("Digite seu gênero (MASCULINO/FEMININO): ").strip().upper()

        if acesso == NIVEL_ADM and genero == GENERO_M:
            print("Olá administrador")
        elif acesso == NIVEL_ADM and genero == GENERO_F:
            print("Olá administradora")
        elif acesso == NIVEL_USR and genero == GENERO_M:
            print("Olá usuário")
        elif acesso == NIVEL_USR and genero == GENERO_F:
            print("Olá usuária")
        else:
            print("Gênero inválido.\nValores aceitos: MASCULINO ou FEMININO")

    elif acesso == NIVEL_GUEST:
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")