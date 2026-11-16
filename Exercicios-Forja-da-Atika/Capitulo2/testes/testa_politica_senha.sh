#!/usr/bin/env bash
# Testes do exercício 1. Ordem das entradas: usuário, senha, confirmação.
cd "$(dirname "$0")" || exit 1
source ./lib.sh
ARQUIVO="../PoliticaSenha.py"
SENHA_OK="cafe com leite as 7h"

titulo "Exercício 1: Política de senha"

# Regra 1: usuário
caso "usuário vazio" \
    $'\n'"$SENHA_OK"$'\n'"$SENHA_OK" \
    "+Cadastro REJEITADO" "-ACEITA"
caso "usuário só com espaços" \
    $'    \n'"$SENHA_OK"$'\n'"$SENHA_OK" \
    "+Cadastro REJEITADO" "-ACEITA"

# Confirmação (regra que você adicionou)
caso "confirmação diferente" \
    $'maria\nSenhaForte2026\nOutraSenha2026' \
    "+Cadastro REJEITADO" "-ACEITA"
caso "confirmação difere só em maiúsculas/minúsculas" \
    $'maria\nSenhaForte2026\nsenhaforte2026' \
    "+Cadastro REJEITADO" "-ACEITA"
caso "confirmação difere só por um espaço no fim" \
    $'maria\nSenhaForte2026 \nSenhaForte2026' \
    "+Cadastro REJEITADO" "-ACEITA"

# Regra 2: tamanho mínimo (limites)
caso "senha com 11 caracteres" \
    $'maria\nabcdefghijk\nabcdefghijk' \
    "+Cadastro REJEITADO" "-ACEITA"
caso "senha com 12 caracteres" \
    $'maria\nabcdefghijkl\nabcdefghijkl' \
    "+Senha ACEITA" "-REJEITADO"
caso "senha com 13 caracteres" \
    $'maria\nabcdefghijklm\nabcdefghijklm' \
    "+Senha ACEITA" "-REJEITADO"
# Decisão sua: uma senha de 12 espaços deve ser aceita? Este caso espera que
# não. Se você decidir aceitar, apague o caso e justifique no comentário.
caso "senha com 12 espaços" \
    $'maria\n            \n            ' \
    "+Cadastro REJEITADO" "-ACEITA"

# Regra 2 antes da regra 3: o motivo precisa citar o mínimo de 12
caso "usuário joao e senha JOAO (o motivo deve ser o tamanho)" \
    $'joao\nJOAO\nJOAO' \
    "+Cadastro REJEITADO" "+12" "-ACEITA"

# Regra 3: senha igual ao usuário
caso "senha igual ao usuário, com outras maiúsculas" \
    $'administrador\nADMINISTRADOR\nADMINISTRADOR' \
    "+Cadastro REJEITADO" "-ACEITA"

# Regra 4: senhas vazadas
caso "senha vazada, igual à da lista" \
    $'maria\nsenha1234567\nsenha1234567' \
    "+Cadastro REJEITADO" "-ACEITA"
caso "senha vazada com maiúsculas misturadas" \
    $'maria\nSeNhA1234567\nSeNhA1234567' \
    "+Cadastro REJEITADO" "-ACEITA"

# Caminho feliz
caso "frase-senha com espaços é aceita" \
    $'maria\n'"$SENHA_OK"$'\n'"$SENHA_OK" \
    "+Senha ACEITA para o usuário maria" "-REJEITADO"
# "+...usuário maria" garante que os espaços do início sumiram;
# "-maria " garante que os do fim também sumiram.
caso "espaços em volta do usuário somem na mensagem" \
    $'  maria  \n'"$SENHA_OK"$'\n'"$SENHA_OK" \
    "+Senha ACEITA para o usuário maria" "-maria "

resumo
