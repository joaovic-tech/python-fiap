#!/usr/bin/env bash
# Testes do exercício 6. Entradas: um evento por linha.
# Se o programa pedir mais eventos do que o caso fornece, ele trava com
# EOFError (Traceback) e o caso falha: o FIM não encerrou o laço.
cd "$(dirname "$0")" || exit 1
source ./lib.sh
ARQUIVO="../MonitorForcaBruta.py"

ALERTA="ALERTA: possível força bruta"
NENHUM="Nenhum evento analisado"

titulo "Exercício 6: Monitor de força bruta"

caso "FIM logo de cara" "FIM" \
    "+$NENHUM" "-Eventos analisados" "-$ALERTA"
caso "só inválidos" $'xyz\nFIM' \
    "+Evento ignorado: XYZ" "+$NENHUM" "-Eventos analisados"
caso "dois OK" $'OK\nOK\nFIM' \
    "+Eventos analisados: 2" "+Falhas: 0" "+Maior sequência de falhas: 0" "+Alertas gerados: 0" "-$NENHUM"
caso "três falhas seguidas" $'FALHA\nFALHA\nFALHA\nFIM' \
    "+$ALERTA no evento 3" "+Alertas gerados: 1" "+Maior sequência de falhas: 3"
caso "cinco falhas seguidas (um alerta só)" $'FALHA\nFALHA\nFALHA\nFALHA\nFALHA\nFIM' \
    "+$ALERTA no evento 3" "-$ALERTA no evento 4" "-$ALERTA no evento 5" \
    "+Alertas gerados: 1" "+Maior sequência de falhas: 5" "+Falhas: 5"
caso "OK quebra a sequência" $'FALHA\nFALHA\nOK\nFALHA\nFIM' \
    "-$ALERTA" "+Falhas: 3" "+Maior sequência de falhas: 2" "+Eventos analisados: 4"
caso "duas sequências, dois alertas" $'FALHA\nFALHA\nFALHA\nOK\nFALHA\nFALHA\nFALHA\nFIM' \
    "+$ALERTA no evento 3" "+$ALERTA no evento 7" "+Alertas gerados: 2"
caso "maior sequência não se perde depois do OK" $'FALHA\nFALHA\nFALHA\nFALHA\nOK\nFALHA\nFIM' \
    "+Maior sequência de falhas: 4" "+Falhas: 5"
caso "inválido no meio não zera nem conta" $'FALHA\nFALHA\nxyz\nFALHA\nFIM' \
    "+Evento ignorado: XYZ" "+$ALERTA no evento 3" "+Eventos analisados: 3"
caso "minúsculas e espaços" $' falha \nfalha\n Falha\n ok \n fim ' \
    "+$ALERTA no evento 3" "+Eventos analisados: 4" "-Evento ignorado"
caso "nada depois do FIM conta" $'FALHA\nFIM\nFALHA\nFALHA' \
    "+Falhas: 1" "+Eventos analisados: 1" "-$ALERTA"
caso "exemplo do enunciado" $'falha\nFALHA\nxyz\nFALHA\nOK\nfim' \
    "+Evento ignorado: XYZ" "+$ALERTA no evento 3" "+Eventos analisados: 4" \
    "+Falhas: 3" "+Maior sequência de falhas: 3" "+Alertas gerados: 1"

resumo
