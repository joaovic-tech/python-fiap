#!/usr/bin/env bash
# Testes do exercício 2. Entrada: número da porta.
cd "$(dirname "$0")" || exit 1
source ./lib.sh
ARQUIVO="../ClassificadorPorta.py"

SYSTEM="System Port (well-known)"
USER_PORT="User Port (registered)"
DYNAMIC="Dynamic/Private Port"
ALERTA="ALERTA: serviço padrão trafega dados sem criptografia"
ROOT="Requer privilégio de root para escutar"

titulo "Exercício 2: Classificador de portas"

# Portas inválidas: nada além de "Porta INVÁLIDA"
caso "porta -1" "-1" \
    "+Porta INVÁLIDA" "-$SYSTEM" "-$USER_PORT" "-$DYNAMIC" "-$ALERTA" "-$ROOT"
caso "porta 65536" "65536" \
    "+Porta INVÁLIDA" "-$SYSTEM" "-$USER_PORT" "-$DYNAMIC" "-$ALERTA" "-$ROOT"

# Toda porta válida sai no formato "Porta N: <faixa>", como no exemplo do
# enunciado. O formato vale para as três faixas, com ou sem alerta.

# System Ports
caso "porta 0" "0" "+Porta 0: $SYSTEM" "+$ROOT" "-$ALERTA" "-INVÁLIDA"
caso "porta 21 (FTP)" "21" "+Porta 21: $SYSTEM" "+$ALERTA" "+$ROOT"
caso "porta 23 (Telnet), exemplo do enunciado" "23" \
    "+Porta 23: $SYSTEM" "+$ALERTA" "+$ROOT"
caso "porta 80 (HTTP)" "80" "+Porta 80: $SYSTEM" "+$ALERTA" "+$ROOT"
caso "porta 443 (HTTPS)" "443" "+Porta 443: $SYSTEM" "+$ROOT" "-$ALERTA"
caso "porta 1023 (limite)" "1023" "+Porta 1023: $SYSTEM" "+$ROOT" "-$USER_PORT"

# User Ports
caso "porta 1024 (limite)" "1024" \
    "+Porta 1024: $USER_PORT" "-$SYSTEM" "-$ROOT" "-$ALERTA"
caso "porta 49151 (limite)" "49151" \
    "+Porta 49151: $USER_PORT" "-$DYNAMIC" "-$ROOT" "-$ALERTA"

# Dynamic Ports
caso "porta 49152 (limite)" "49152" \
    "+Porta 49152: $DYNAMIC" "-$USER_PORT" "-$ROOT" "-$ALERTA"
caso "porta 65535 (limite)" "65535" \
    "+Porta 65535: $DYNAMIC" "-INVÁLIDA" "-$ROOT" "-$ALERTA"

# A constante do enunciado tem só 21, 23 e 80. Com o script como está, a 8080
# é uma User Port comum: sem alerta.
caso "porta 8080 no script original (não está no enunciado: sem alerta)" "8080" \
    "+Porta 8080: $USER_PORT" "-$ALERTA" "-$ROOT"

# Independência das regras: e se a 8080 (HTTP alternativo, sem criptografia)
# entrasse na constante? O teste roda uma CÓPIA temporária do seu script com
# a 8080 acrescentada logo depois da linha da constante. Seu arquivo não muda.
# A 8080 é User Port: deve ter ALERTA e não deve exigir root.
COPIA=$(mktemp --suffix=.py)
trap 'rm -f "$COPIA"' EXIT
if grep -q '^PORTAS_SEM_CRIPTOGRAFIA *=' "$ARQUIVO"; then
    sed '/^PORTAS_SEM_CRIPTOGRAFIA *=/a PORTAS_SEM_CRIPTOGRAFIA = PORTAS_SEM_CRIPTOGRAFIA + (8080,)' \
        "$ARQUIVO" > "$COPIA"
    ORIGINAL="$ARQUIVO"
    ARQUIVO="$COPIA"
    caso "porta 8080 adicionada à constante (regra 2 independente da faixa)" "8080" \
        "+Porta 8080: $USER_PORT" "+$ALERTA" "-$ROOT" "-$SYSTEM"
    ARQUIVO="$ORIGINAL"
else
    FALHOU=$((FALHOU + 1))
    echo "  ${VERMELHO}FALHOU${RESET}  porta 8080: constante PORTAS_SEM_CRIPTOGRAFIA não encontrada no início de uma linha"
fi

resumo
