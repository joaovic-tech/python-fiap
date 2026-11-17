"""
O seu módulo solicitará o nível de acesso de uma pessoa que pode ser:
ADM, USR ou GUEST e o gênero dessa pessoa,

- caso o nível seja ADM, ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres.
- Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres.
- Se o nível for GUEST, a mensagem deverá ser “Olá visitante”.
- E se o nível digitado for diferente de ADM, USR ou GUEST deverá exibir a mensagem “Olá desconhecido(a)”.
Considere apenas os gêneros masculino e feminino
"""

NIVEL_ADM = "ADM"
NIVEL_USR = "USR"
NIVEL_GUEST = "GUEST"
GENERO_M = "MASCULINO"
GENERO_F = "FEMININO"

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