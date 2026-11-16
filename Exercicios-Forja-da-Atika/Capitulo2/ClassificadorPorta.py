"""
EXERCÍCIO 2: CLASSIFICADOR DE PORTAS DE REDE

Contexto:
    Durante uma varredura de rede, você encontrou uma porta aberta e precisa
    classificá-la para o relatório.

Entrada:
    - Número da porta (inteiro)

Regra 1: faixa da porta (segundo a RFC 6335, da IANA):
    - 0 a 1023 ........ "System Port (well-known)"
    - 1024 a 49151 .... "User Port (registered)"
    - 49152 a 65535 ... "Dynamic/Private Port"
    - Qualquer outro valor: "Porta INVÁLIDA". Nesse caso, nada mais é exibido.

Regra 2: protocolo sem criptografia (independente da regra 1):
    Se a porta for 21 (FTP), 23 (Telnet) ou 80 (HTTP), exiba também:
    "ALERTA: serviço padrão trafega dados sem criptografia"
    Guarde essas portas numa constante.

Regra 3: privilégio (independente das regras 1 e 2):
    Em sistemas Linux, abrir uma porta abaixo de 1024 exige privilégio de root.
    Se for o caso, exiba: "Requer privilégio de root para escutar"

Exemplo de saída para a porta 23:
    Porta 23: System Port (well-known)
    ALERTA: serviço padrão trafega dados sem criptografia
    Requer privilégio de root para escutar

Atenção:
    As regras 2 e 3 são INDEPENDENTES da regra 1, assim como sala e
    prioridade eram independentes no exercício da triagem. Pense antes de
    aninhar tudo num único if/elif.

Casos que você deve testar, no mínimo:
    -1, 0, 21, 23, 80, 443, 1023, 1024, 49151, 49152, 65535, 65536

Permitido: if, elif, else, and, or, not, in, input(), int(), print(),
f-strings, tuplas, constantes, comparações encadeadas.
Proibido: for, while, def, try.
"""
# TODO (fim do curso): refatorar este exercício usando todo o conhecimento
# adquirido até lá e comparar com esta versão, para medir minha evolução.
# Não apagar a versão atual: ela é o registro do meu nível hoje.

# Mensagens padrões
INVALIDA = "Porta INVÁLIDA"
SYSTEM="System Port (well-known)"
USER_PORT="User Port (registered)"
DYNAMIC="Dynamic/Private Port"
ALERTA="ALERTA: serviço padrão trafega dados sem criptografia"
ROOT="Requer privilégio de root para escutar"

# Portas padrões
PORTAS_SEM_CRIPTOGRAFIA = (21, 23, 80)

porta_encontrada = int(input("Digite o número da porta encontrada: "))
porta_negativa = porta_encontrada < 0

if porta_negativa or porta_encontrada >= 65536:
    print(INVALIDA)
elif porta_encontrada in PORTAS_SEM_CRIPTOGRAFIA:
    if 0 <= porta_encontrada <= 1023:
        print(f"Porta {porta_encontrada}: {SYSTEM}")
    elif 1024 <= porta_encontrada <= 49151:
        print(f"Porta {porta_encontrada}: {USER_PORT}")
    elif 49152 <= porta_encontrada <= 65535:
        print(f"Porta {porta_encontrada}: {DYNAMIC}")

    print(ALERTA)

    if porta_encontrada < 1024:
        print(ROOT)
elif 0 <= porta_encontrada <= 1023:
    print(f"Porta {porta_encontrada}: {SYSTEM}")
    print(ROOT)
elif 1024 <= porta_encontrada <= 49151:
    print(f"Porta {porta_encontrada}: {USER_PORT}")
elif 49152 <= porta_encontrada <= 65535:
    print(f"Porta {porta_encontrada}: {DYNAMIC}")
else:
    print("Não era para chegar a esse ponto, errei como dev fui mlk ;(")