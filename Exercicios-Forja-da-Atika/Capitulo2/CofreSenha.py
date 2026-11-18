""" TODO: DEPOIS IREI RETORNAR AQUI PARA REFATORAR USANDO TODO O CONHECIMENTO ADQUIRIDO NOS ESTUDOS DA FIAP
EXERCÍCIO 4: COFRE COM TENTATIVAS LIMITADAS (while)
Contexto:
    Um cofre digital guarda as credenciais do time de segurança. Quem errar a
    senha várias vezes seguidas está, possivelmente, tentando adivinhar. O cofre
    precisa dar um número limitado de chances e depois travar.
Entrada (repetida dentro do laço):
    - Senha
Regras:
    1. A senha correta e o número máximo de tentativas ficam em CONSTANTES
       (use senha correta "Forja@2026" e máximo de 3 tentativas).
    2. A comparação é EXATA: sem strip() e sem upper(). "forja@2026" e
       " Forja@2026" são senhas erradas (mesma decisão do Exercício 1: a senha
       fica intacta).
    3. Senha VAZIA (o usuário só apertou Enter, nenhum caractere) não conta
       como tentativa. Mostre "Senha vazia não conta como tentativa" e peça
       de novo. Atenção: "   " (só espaços) NÃO é vazia, é uma senha errada.
    4. Senha errada: mostre "Senha INCORRETA. Tentativas restantes: <N>".
    5. Senha correta: mostre "Acesso LIBERADO" e PARE de pedir senha.
    6. Acabaram as tentativas: mostre "Cofre BLOQUEADO" e PARE de pedir senha.
Exemplo:
    Senha: abc
    Senha INCORRETA. Tentativas restantes: 2
    Senha:
    Senha vazia não conta como tentativa
    Senha: Forja@2026
    Acesso LIBERADO
Armadilhas:
    - Depois de LIBERADO ou BLOQUEADO, o programa não pode pedir mais nenhuma
      senha. Se pedir, o laço está com a condição de parada errada.
    - Quem digitar a senha certa DEPOIS do bloqueio não pode entrar.
    - A contagem de tentativas restantes não pode ficar negativa nem pular
      números por causa da senha vazia.
Pergunta de projeto (responda num comentário antes de escrever o código):
    Você vai encerrar o laço pela condição do while ou com break? Por quê?
    As duas formas funcionam. Escolha uma e defenda.
Casos que você deve testar, no mínimo:
    - Senha certa de primeira
    - Duas erradas e a certa na terceira (limite!)
    - Três erradas
    - Três erradas e depois a certa (não pode liberar)
    - Duas vazias, depois a certa (vazias não gastam tentativa)
    - "forja@2026" (minúsculas) e " Forja@2026" (espaço na frente)
Permitido:
    while, break, True, False, if, elif, else, and, or, not, in,
    input(), print(), len(), str(), f-strings, tuplas, constantes,
    contador = contador + 1 (como no while_infinito.py).
Proibido:
    for, def, try, continue, listas, +=. Ainda não chegamos lá.
"""

# Irei usar as duas porque a condição do while irá cuidar do esgotamento das tentativas e o break cuida do sucesso.

SENHA_DO_COFRE = "Forja@2026"
MAXIMO_DE_TENTATIVAS = 3

tentativas_restantes = MAXIMO_DE_TENTATIVAS
acesso_liberado = False

while tentativas_restantes > 0:
    senha_digitada = input("Senha: ")

    if not senha_digitada:
        print("Senha vazia não conta como tentativa")
    elif senha_digitada == SENHA_DO_COFRE:
        print("Acesso LIBERADO")
        acesso_liberado = True
        break
    else:
        tentativas_restantes = tentativas_restantes - 1
        print(f"Senha INCORRETA. Tentativas restantes: {tentativas_restantes}")

if not acesso_liberado:
    print("Cofre BLOQUEADO")