"""
EXERCÍCIO 5: VARREDURA DE UMA FAIXA DE PORTAS (for + range)

Contexto:
    Antes de um pentest autorizado, você precisa listar uma faixa de portas,
    classificar cada uma e destacar as que costumam expor serviços sensíveis.
    Nada de rede aqui: o programa só classifica os números.

Entradas:
    - Porta inicial (inteiro)
    - Porta final (inteiro)

Validação (se falhar, mostre "DADOS INVÁLIDOS" e o motivo, e NÃO varra nada):
    - As duas portas devem estar entre 1 e 65535
    - A porta inicial não pode ser maior que a final
    - A faixa pode ter no máximo 20 portas, CONTANDO as duas pontas
      (1 a 20 é válido; 1 a 21 não é)

Para cada porta da faixa, INCLUINDO a porta final, mostre uma linha:
    "Porta <N>: <classe>"
    Classes (as mesmas do Exercício 2):
    - 1 a 1023 ......... "bem conhecida"
    - 1024 a 49151 ..... "registrada"
    - 49152 a 65535 .... "dinâmica"
    Se a porta estiver na tupla de portas sensíveis (21, 22, 23, 445, 3389),
    acrescente " [SENSÍVEL]" no fim da linha.

Ao final da varredura, mostre:
    "Total de portas analisadas: <N>"
    "Portas sensíveis encontradas: <M>"
    Se M for zero, mostre também "Nenhuma porta sensível na faixa".

Exemplo:
    porta inicial 20, porta final 23
    Porta 20: bem conhecida
    Porta 21: bem conhecida [SENSÍVEL]
    Porta 22: bem conhecida [SENSÍVEL]
    Porta 23: bem conhecida [SENSÍVEL]
    Total de portas analisadas: 4
    Portas sensíveis encontradas: 3

Armadilhas:
    - Rode o seu exemplo_for.py com fim = 5 e conte quantos números aparecem.
      O range() tem uma regra sobre o valor final. Descubra qual é antes de
      escrever este exercício, senão a porta final some da varredura.
    - O limite de 20 portas também conta as duas pontas. 1 a 20 são quantas
      portas? Faça a conta antes de escrever o if.
    - Os contadores são iniciados ANTES do laço. Pense no porquê.

Constantes obrigatórias (nada de número mágico no meio do código):
    - Menor e maior porta válida
    - Os limites entre as classes
    - O tamanho máximo da faixa
    - A tupla de portas sensíveis

Casos que você deve testar, no mínimo:
    - 20 a 25 (a 25 tem que aparecer)
    - 1020 a 1027 (fronteira 1023/1024, nenhuma sensível)
    - 49150 a 49153 (fronteira 49151/49152)
    - 65530 a 65535 (última porta possível)
    - 22 a 22 (faixa de uma porta só)
    - 1 a 20 (limite aceito) e 1 a 21 (limite recusado)
    - 0 a 5, 65535 a 65536 e 30 a 20 (inválidos)

Observação: texto em vez de número no input() ainda trava o programa
(ValueError). Deixe um comentário TODO perto dos input() para tratar isso
quando chegarmos em try/except.

Permitido: for, range(), if, elif, else, and, or, not, in, input(), int(),
str(), print(), f-strings, tuplas, constantes,
contador = contador + 1 (como no while_infinito.py).
Proibido: while, def, try, continue, listas, +=. Ainda não chegamos lá.
"""
