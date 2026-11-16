"""
EXERCÍCIO 1: POLÍTICA DE SENHA

Contexto:
    O time de segurança da sua empresa precisa de um script que verifique se
    uma senha nova atende à política mínima antes de ser cadastrada.

Entradas:
    - Nome de usuário
    - Senha

Regras (a senha é REJEITADA se qualquer uma falhar):
    1. O usuário não pode ser vazio.
    2. A senha deve ter no mínimo 12 caracteres.
    3. A senha não pode ser igual ao nome de usuário, ignorando maiúsculas e
       minúsculas ("Admin" e "ADMIN" contam como iguais).
    4. A senha não pode estar numa lista de senhas vazadas conhecidas. Crie uma
       constante com pelo menos 5 senhas, por exemplo: "123456789012",
       "senha1234567", "qwertyuiopas", "admin1234567", "iloveyou1234".
       A comparação também ignora maiúsculas e minúsculas.

Saída:
    - Se a senha for aceita: "Senha ACEITA para o usuário <USUÁRIO>"
    - Se for rejeitada: "Cadastro REJEITADA" e o MOTIVO. Diga qual regra falhou,
      não liste todas.

Pergunta de projeto (responda num comentário antes de escrever o código):
    Você deve aplicar strip() na SENHA? E no USUÁRIO? Justifique.
    Dica: um espaço no fim da senha faz parte dela ou é erro de digitação?

Casos que você deve testar, no mínimo:
    - Usuário vazio
    - Senha com 11, 12 e 13 caracteres (limites!)
    - Usuário "joao" e senha "JOAO" (fica abaixo de 12, então qual regra deve
      aparecer primeiro?)
    - Usuário e senha iguais com 12 caracteres ou mais
    - Uma senha da lista com letras maiúsculas misturadas

Permitido: if, elif, else, and, or, not, in, input(), print(), len(),
.upper(), .strip(), f-strings, tuplas, constantes.
Proibido: for, while, def, try. Ainda não chegamos lá.
"""
# TODO (fim do curso): refatorar este exercício usando todo o conhecimento
# adquirido até lá e comparar com esta versão, para medir minha evolução.
# Não apagar a versão atual: ela é o registro do meu nível hoje.

"""
RESPOSTA SOBRE O USO DO STRIP()

    Irei colocar o strip() somente no usuário, se o usuário optar
    por criar uma senha-frase ele pode e para prevenir que ele digitou errado
    um espaço no final irei por dois campos para o sistema ter certeza que ele
    quer realmente por espaços tanto no início quanto no final da senha.
"""

SENHAS_VAZADAS = ("123456789012","senha1234567", "qwertyuiopas", "admin1234567", "iloveyou1234")
DEFAULT_MSG_ERRO = "Cadastro REJEITADO!!!\nMOTIVO:"

print(" "+"-"*62)
print("|" + " "*62 + "|")
print("|  " + " "*20 + "CADASTRO DE USUÁRIO" + " "*20 + " |")
print("|" + " "*62 + "|")
print("|    " + "REQUISITOS: " + " " * 46 + "|")
print("|    " + "   - O usuário não pode ser vazio." + " " * 24 + "|")
print("|    " + "   - A senha deve ter no mínimo 12 caracteres." + " " * 12 + "|")
print("|    " + "   - A senha não pode ser igual ao nome de usuário" + " " * 8 + "|")
print(" "+"-"*62)

usuario = input("usuário: ").strip()
senha = input("senha: ")
confirma_senha = input("confirme novamente a senha: ")

senha_vazia = len(senha.strip()) == 0

if not usuario:
    print(f"{DEFAULT_MSG_ERRO} O usuário não pode ser vazio.")
elif senha_vazia:
    print(f"{DEFAULT_MSG_ERRO} A senha não pode ser vazia")
elif senha != confirma_senha:
    print(f"{DEFAULT_MSG_ERRO} A senha de confirmação está incorreta, tente novamente!")
elif len(senha) < 12:
    print(f"{DEFAULT_MSG_ERRO} A senha deve ter no mínimo 12 caracteres e a sua tem {len(senha)}")
elif usuario.upper() == senha.upper():
    print(f"{DEFAULT_MSG_ERRO} A senha não pode ser o mesmo nome do usuário")
elif senha.lower() in SENHAS_VAZADAS:
    print(f"{DEFAULT_MSG_ERRO} A senha digitada já foi vazada, use outra")
else:
    print(f"Senha ACEITA para o usuário {usuario}")