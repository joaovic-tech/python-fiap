#!/usr/bin/env bash
# Testes do exercício 4. Entradas: uma senha por linha.
# Se o programa pedir mais senhas do que o caso fornece, ele trava com
# EOFError (Traceback) e o caso falha: o laço não parou quando devia.
cd "$(dirname "$0")" || exit 1
source ./lib.sh
ARQUIVO="../CofreSenha.py"

CERTA="Forja@2026"
LIBERADO="Acesso LIBERADO"
BLOQUEADO="Cofre BLOQUEADO"
INCORRETA="Senha INCORRETA"
VAZIA="Senha vazia não conta como tentativa"

titulo "Exercício 4: Cofre com tentativas limitadas"

caso "certa de primeira" "$CERTA" \
    "+$LIBERADO" "-$INCORRETA" "-$BLOQUEADO"
caso "uma errada e a certa" $'abc\n'"$CERTA" \
    "+Tentativas restantes: 2" "+$LIBERADO" "-$BLOQUEADO"
caso "duas erradas e a certa na terceira (limite)" $'abc\ndef\n'"$CERTA" \
    "+Tentativas restantes: 1" "+$LIBERADO" "-$BLOQUEADO"
caso "três erradas" $'abc\ndef\nghi' \
    "+Tentativas restantes: 0" "+$BLOQUEADO" "-$LIBERADO"
caso "três erradas e a certa depois do bloqueio" $'abc\ndef\nghi\n'"$CERTA" \
    "+$BLOQUEADO" "-$LIBERADO"
caso "duas vazias e a certa" $'\n\n'"$CERTA" \
    "+$VAZIA" "+$LIBERADO" "-$INCORRETA"
caso "vazias não gastam tentativa" $'\nabc\n\ndef\n'"$CERTA" \
    "+Tentativas restantes: 1" "+$LIBERADO" "-$BLOQUEADO" "-Tentativas restantes: 0"
caso "minúsculas contam como errada" $'forja@2026\n'"$CERTA" \
    "+Tentativas restantes: 2" "+$LIBERADO"
caso "espaço na frente conta como errada" $' Forja@2026\n'"$CERTA" \
    "+Tentativas restantes: 2" "+$LIBERADO"
caso "só espaços conta como errada (não é vazia)" $'   \n'"$CERTA" \
    "+Tentativas restantes: 2" "-$VAZIA" "+$LIBERADO"
caso "nunca negativa" $'a\nb\nc' \
    "-Tentativas restantes: -1" "+$BLOQUEADO"

resumo
