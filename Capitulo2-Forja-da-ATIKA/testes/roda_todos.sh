#!/usr/bin/env bash
# Roda os testes de todos os exercícios. Para rodar só um exercício, execute o
# script dele diretamente (ex.: ./testa_politica_senha.sh).
cd "$(dirname "$0")" || exit 1

codigo=0
for script in testa_politica_senha.sh testa_classificador_porta.sh testa_bloqueio_login.sh; do
    bash "$script" || codigo=1
done
exit "$codigo"
