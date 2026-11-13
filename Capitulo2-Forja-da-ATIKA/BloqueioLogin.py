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
# TODO (fim do curso): refatorar este exercício usando todo o conhecimento
# adquirido até lá e comparar com esta versão, para medir minha evolução.
# Não apagar a versão atual: ela é o registro do meu nível hoje.
