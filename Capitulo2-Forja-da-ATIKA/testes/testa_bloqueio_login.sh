#!/usr/bin/env bash
# Testes do exercício 3. Ordem das entradas: usuário, tentativas, dispositivo, hora.
cd "$(dirname "$0")" || exit 1
source ./lib.sh
ARQUIVO="../BloqueioLogin.py"

INVALIDO="DADOS INVÁLIDOS"
LIBERADA="Conta LIBERADA"
MFA="Exigir MFA (segundo fator)"
BLOQUEADA="Conta BLOQUEADA"
ALERTA="ALERTA SOC"

titulo "Exercício 3: Bloqueio de login"

# Validação: nada além de DADOS INVÁLIDOS
caso "usuário vazio" $'\n0\nSIM\n10' \
    "+$INVALIDO" "-$LIBERADA" "-$ALERTA"
caso "usuário só com espaços" $'   \n0\nSIM\n10' \
    "+$INVALIDO" "-$LIBERADA" "-$ALERTA"
caso "tentativas -1" $'maria\n-1\nSIM\n10' \
    "+$INVALIDO" "-$LIBERADA" "-$ALERTA"
caso "dispositivo TALVEZ" $'maria\n0\nTALVEZ\n10' \
    "+$INVALIDO" "-$LIBERADA" "-$ALERTA"
caso "hora -1" $'maria\n0\nNAO\n-1' \
    "+$INVALIDO" "-$LIBERADA" "-$ALERTA"
caso "hora 24" $'maria\n0\nNAO\n24' \
    "+$INVALIDO" "-$LIBERADA" "-$ALERTA"

# Decisão A: estado da conta (dispositivo conhecido, horário comercial)
caso "0 tentativas" $'maria\n0\nSIM\n10' "+$LIBERADA" "-$MFA" "-$BLOQUEADA"
caso "2 tentativas (limite)" $'maria\n2\nSIM\n10' "+$LIBERADA" "-$MFA"
caso "3 tentativas (limite)" $'maria\n3\nSIM\n10' "+$MFA" "-$LIBERADA"
caso "4 tentativas (limite)" $'maria\n4\nSIM\n10' "+$MFA" "-$BLOQUEADA"
caso "5 tentativas (limite)" $'maria\n5\nSIM\n10' "+$BLOQUEADA" "-$MFA"

# Decisão B: alerta (dispositivo desconhecido fora do expediente)
caso "desconhecido às 0h" $'maria\n0\nNAO\n0' "+$ALERTA" "-$INVALIDO"
caso "desconhecido às 6h" $'maria\n0\nNAO\n6' "+$ALERTA"
caso "desconhecido às 7h (limite)" $'maria\n0\nNAO\n7' "-$ALERTA" "-$INVALIDO"
caso "desconhecido às 19h" $'maria\n0\nNAO\n19' "-$ALERTA"
caso "desconhecido às 20h (limite)" $'maria\n0\nNAO\n20' "+$ALERTA"
caso "desconhecido às 23h" $'maria\n0\nNAO\n23' "+$ALERTA" "-$INVALIDO"
caso "conhecido de madrugada" $'maria\n0\nSIM\n2' "-$ALERTA"
caso "desconhecido às 10h" $'maria\n0\nNAO\n10' "-$ALERTA"

# Normalização da resposta do dispositivo
caso "dispositivo 'não' minúsculo e com acento" $'maria\n0\nnão\n2' \
    "+$ALERTA" "-$INVALIDO"
caso "dispositivo ' sim ' com espaços" $'maria\n0\n sim \n2' \
    "+$LIBERADA" "-$ALERTA" "-$INVALIDO"

# Exemplo do enunciado
caso "exemplo: maria, 3, NAO, 2h" $'maria\n3\nNAO\n2' \
    "+$MFA" "+ALERTA SOC: acesso suspeito de MARIA"

resumo
