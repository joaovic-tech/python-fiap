#!/usr/bin/env bash
# Testes do exercício 5. Ordem das entradas: porta inicial, porta final.
cd "$(dirname "$0")" || exit 1
source ./lib.sh
ARQUIVO="../VarreduraPortas.py"

INVALIDO="DADOS INVÁLIDOS"
TOTAL="Total de portas analisadas"
SENSIVEIS="Portas sensíveis encontradas"
NENHUMA="Nenhuma porta sensível na faixa"

titulo "Exercício 5: Varredura de portas"

# Validação: nada de varredura
caso "porta 0" $'0\n5' "+$INVALIDO" "-Porta 1:" "-$TOTAL"
caso "porta 65536" $'65535\n65536' "+$INVALIDO" "-Porta 65535:" "-$TOTAL"
caso "inicial maior que final" $'30\n20' "+$INVALIDO" "-$TOTAL"
caso "21 portas (acima do limite)" $'1\n21' "+$INVALIDO" "-Porta 1:" "-$TOTAL"

# Faixas válidas
caso "1 a 20 (limite aceito)" $'1\n20' \
    "-$INVALIDO" "+Porta 1: bem conhecida" "+Porta 20: bem conhecida" "+$TOTAL: 20" "+$SENSIVEIS: 0" "+$NENHUMA"
caso "20 a 25 (porta final incluída)" $'20\n25' \
    "+Porta 20: bem conhecida" "+Porta 25: bem conhecida" "-Porta 26" "-Porta 19" \
    "+Porta 21: bem conhecida [SENSÍVEL]" "+Porta 22: bem conhecida [SENSÍVEL]" \
    "+Porta 23: bem conhecida [SENSÍVEL]" "-Porta 24: bem conhecida [SENSÍVEL]" \
    "+$TOTAL: 6" "+$SENSIVEIS: 3" "-$NENHUMA"
caso "1020 a 1027 (fronteira 1023/1024)" $'1020\n1027' \
    "+Porta 1023: bem conhecida" "+Porta 1024: registrada" "+Porta 1027: registrada" \
    "+$TOTAL: 8" "+$NENHUMA"
caso "49150 a 49153 (fronteira 49151/49152)" $'49150\n49153' \
    "+Porta 49151: registrada" "+Porta 49152: dinâmica" "+Porta 49153: dinâmica" "+$TOTAL: 4"
caso "65530 a 65535 (última porta)" $'65530\n65535' \
    "+Porta 65535: dinâmica" "+$TOTAL: 6" "-$INVALIDO"
caso "22 a 22 (uma porta só)" $'22\n22' \
    "+Porta 22: bem conhecida [SENSÍVEL]" "+$TOTAL: 1" "+$SENSIVEIS: 1"
caso "3380 a 3390 (RDP)" $'3380\n3390' \
    "+Porta 3389: registrada [SENSÍVEL]" "-Porta 3388: registrada [SENSÍVEL]" "+$SENSIVEIS: 1"
caso "440 a 450 (SMB)" $'440\n450' \
    "+Porta 445: bem conhecida [SENSÍVEL]" "+$TOTAL: 11" "+$SENSIVEIS: 1"

resumo
