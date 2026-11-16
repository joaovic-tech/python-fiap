"""
EXERCÍCIO 3: BLOQUEIO DE LOGIN E ALERTA DE ACESSO SUSPEITO

Contexto:
    O sistema de autenticação registra cada tentativa de login. Você vai
    decidir o que fazer com a conta e se o acesso merece um alerta para o SOC.

Entradas:
    - Nome de usuário
    - Quantidade de tentativas de senha erradas seguidas (inteiro)
    - O dispositivo é conhecido? (SIM/NAO, aceite também NÃO)
    - Hora do acesso (inteiro de 0 a 23)

Validação (se qualquer uma falhar, mostre "DADOS INVÁLIDOS" e o motivo):
    - Usuário não pode ser vazio
    - Tentativas não pode ser negativo
    - Resposta do dispositivo deve ser SIM ou NAO/NÃO
    - Hora deve estar entre 0 e 23

Decisão A: estado da conta
    - 0 a 2 tentativas ... "Conta LIBERADA"
    - 3 a 4 tentativas ... "Exigir MFA (segundo fator)"
    - 5 ou mais .......... "Conta BLOQUEADA"

Decisão B: alerta de acesso suspeito (independente da decisão A)
    Gere "ALERTA SOC: acesso suspeito de <USUÁRIO>" quando:
    - O dispositivo NÃO for conhecido E
    - A hora estiver FORA do expediente (antes das 7h OU a partir das 20h)

Exemplo:
    usuário "maria", 3 tentativas, dispositivo NAO, hora 2
    -> Exigir MFA (segundo fator)
    -> ALERTA SOC: acesso suspeito de MARIA

Armadilha:
    A condição da decisão B mistura "E" e "OU". Você já viu nesse projeto o
    que acontece com a precedência entre and e or. Use parênteses para que a
    intenção fique explícita.

Constantes obrigatórias (nada de número mágico no meio do código):
    - O limite para exigir MFA
    - O limite para bloquear
    - O início e o fim do expediente
    - As respostas válidas do dispositivo

Casos que você deve testar, no mínimo:
    - Tentativas: -1, 0, 2, 3, 4, 5
    - Horas: -1, 0, 6, 7, 19, 20, 23, 24
    - Dispositivo conhecido de madrugada (não deve gerar alerta)
    - Dispositivo desconhecido às 10h (não deve gerar alerta)

Permitido: if, elif, else, and, or, not, in, input(), int(), print(),
.upper(), .strip(), f-strings, tuplas, constantes.
Proibido: for, while, def, try.
"""
# TODO (fim do curso): Criar uma ValueError para tratamento de dados e refatorar todo o código

# CONSTANTES
RESPOSTAS_SIM = "SIM"
RESPOSTAS_NAO = ("NAO", "NÃO")
MFA_MIN = 3
MFA_MAX = 4
HORA_ACESSO_MIN = 0
HORA_ACESSO_MAX = 23
INICIO_EXPEDIENTE = 7
FIM_EXPEDIENTE = 20

usuario = input("Nome de usuário: ").strip()
qtd_tentativas = int(input("Quantidade de tentativas de senha erradas: "))
resposta_dispositivo = input("O dispositivo é conhecido? (SIM/NÃO): ").strip().upper()
hora_acesso = int(input("Hora do acesso: "))

existe_erro = False

if not usuario:
    print("DADOS INVÁLIDOS\nMotivo: Nome de usuário não pode ser vazio")
    existe_erro = True
if qtd_tentativas < 0:
    print(f"DADOS INVÁLIDOS\nMotivo: Tentativas \"{qtd_tentativas}\" é um valor negativo")
    existe_erro = True

if resposta_dispositivo != RESPOSTAS_SIM and resposta_dispositivo not in RESPOSTAS_NAO:
    print("DADOS INVÁLIDOS\nMotivo: Digite SIM ou NÃO em: \"dispositivo é conhecido?\"")
    existe_erro = True
if hora_acesso < HORA_ACESSO_MIN or hora_acesso > HORA_ACESSO_MAX:
    print(f"DADOS INVÁLIDOS\nMotivo: A hora deve ser entre {HORA_ACESSO_MIN} e {HORA_ACESSO_MAX}")
    existe_erro = True

if not existe_erro:
    dispositivo_conhecido = resposta_dispositivo == RESPOSTAS_SIM
    fora_do_expediente = hora_acesso < INICIO_EXPEDIENTE or hora_acesso >= FIM_EXPEDIENTE

    if MFA_MIN <= qtd_tentativas <= MFA_MAX:
        resultado_conta = "Exigir MFA (segundo fator)"
    elif qtd_tentativas > MFA_MAX:
        resultado_conta = "Conta BLOQUEADA"
    else:
        resultado_conta = "Conta LIBERADA"

    print("-" * 19)
    print("RESULTADO DA CONTA:")
    print(resultado_conta)

    if not dispositivo_conhecido and fora_do_expediente:
        print(f"ALERTA SOC: acesso suspeito de {usuario.upper()}")