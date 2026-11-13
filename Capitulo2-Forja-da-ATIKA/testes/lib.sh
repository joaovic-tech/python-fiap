#!/usr/bin/env bash
# Funções comuns aos testes. Não execute este arquivo: ele é carregado pelos
# outros scripts com "source".

PYTHON="${PYTHON:-python3}"
PASSOU=0
FALHOU=0

if [ -t 1 ]; then
    VERDE=$'\e[32m'; VERMELHO=$'\e[31m'; NEGRITO=$'\e[1m'; RESET=$'\e[0m'
else
    VERDE=''; VERMELHO=''; NEGRITO=''; RESET=''
fi

titulo() {
    echo "${NEGRITO}== $1 ($ARQUIVO)${RESET}"
}

# Uso:
#   caso "descrição" "entradas, uma por linha" "+texto esperado" "-texto proibido" ...
#
# Cada regra começa com "+" (a saída DEVE conter o texto) ou "-" (a saída NÃO
# PODE conter o texto). A comparação é literal e diferencia maiúsculas de
# minúsculas, porque o enunciado define as mensagens exatas.
caso() {
    local descricao="$1" entrada="$2"
    shift 2

    local saida
    saida=$(printf '%s\n' "$entrada" | "$PYTHON" "$ARQUIVO" 2>&1)

    local falhas=() regra texto
    for regra in "$@"; do
        texto="${regra:1}"
        case "$regra" in
            +*) grep -qF -- "$texto" <<<"$saida" || falhas+=("deveria conter: \"$texto\"") ;;
            -*) grep -qF -- "$texto" <<<"$saida" && falhas+=("não deveria conter: \"$texto\"") ;;
        esac
    done
    if grep -q "Traceback" <<<"$saida"; then
        falhas+=("o programa travou (Traceback)")
    fi

    if [ ${#falhas[@]} -eq 0 ]; then
        PASSOU=$((PASSOU + 1))
        echo "  ${VERDE}PASSOU${RESET}  $descricao"
    else
        FALHOU=$((FALHOU + 1))
        echo "  ${VERMELHO}FALHOU${RESET}  $descricao"
        local f
        for f in "${falhas[@]}"; do
            echo "          - $f"
        done
        echo "          entradas (entre colchetes, para mostrar os espaços):"
        while IFS= read -r linha; do
            echo "            [$linha]"
        done <<<"$entrada"
        echo "          saída do programa:"
        sed 's/^/            | /' <<<"$saida"
    fi
}

resumo() {
    echo "  Resultado: ${VERDE}$PASSOU passaram${RESET}, ${VERMELHO}$FALHOU falharam${RESET}"
    echo
    [ "$FALHOU" -eq 0 ]
}
