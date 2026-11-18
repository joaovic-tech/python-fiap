"""
EXERCÍCIO 6: MONITOR DE FORÇA BRUTA (while com sentinela)

Contexto:
    O analista do SOC lê um log de autenticação e digita os eventos, um por
    vez. O programa precisa contar as falhas e disparar um alerta quando
    houver falhas SEGUIDAS demais, que é o rastro de um ataque de força bruta.

Entrada (repetida dentro do laço):
    - Evento: "OK", "FALHA" ou "FIM"
      Aceite minúsculas e espaços em volta (" falha " vale como FALHA).

Regras:
    1. "FIM" encerra a leitura. Nada digitado depois disso pode ser contado.
    2. "OK" é um evento válido e ZERA a sequência de falhas seguidas.
    3. "FALHA" é um evento válido, soma uma falha e aumenta a sequência.
    4. Quando a sequência chegar a 3 (constante), mostre:
       "ALERTA: possível força bruta no evento <N>"
       em que N é a posição do evento entre os eventos VÁLIDOS (OK e FALHA).
       O alerta sai UMA vez por sequência: a 4ª e a 5ª falha seguidas não
       geram alerta novo. Depois de um OK, uma nova sequência de 3 gera outro.
    5. Qualquer outra coisa mostra "Evento ignorado: <VALOR>" (já em
       maiúsculas e sem espaços), não é contada e NÃO zera a sequência.

Ao final, mostre:
    "Eventos analisados: <N>"
    "Falhas: <F>"
    "Maior sequência de falhas: <S>"
    "Alertas gerados: <A>"
    Se nenhum evento válido foi digitado, mostre só "Nenhum evento analisado".

Exemplo:
    Evento (OK/FALHA/FIM): falha
    Evento (OK/FALHA/FIM): FALHA
    Evento (OK/FALHA/FIM): xyz
    Evento ignorado: XYZ
    Evento (OK/FALHA/FIM): FALHA
    ALERTA: possível força bruta no evento 3
    Evento (OK/FALHA/FIM): OK
    Evento (OK/FALHA/FIM): fim
    Eventos analisados: 4
    Falhas: 3
    Maior sequência de falhas: 3
    Alertas gerados: 1

Armadilhas:
    - "Sequência atual" e "maior sequência" são variáveis diferentes. Quando
      o OK zera a atual, a maior não pode ser perdida.
    - Comparar a sequência com >= dispara o alerta em toda falha a partir da
      3ª. Releia a regra 4.
    - Você já escreveu um while que pergunta se o usuário quer sair
      (DesafioDecisaoWhile.py). Compare a condição daquele while com a
      variável que ele testa: ela começa como True e depois vira texto.
      Não repita isso aqui. Uma variável, um tipo.

Constantes obrigatórias:
    - O tamanho da sequência que gera alerta
    - Os textos "OK", "FALHA" e "FIM"

Casos que você deve testar, no mínimo:
    - FIM logo de cara
    - FALHA, FALHA, FALHA (alerta no evento 3)
    - Cinco FALHAs seguidas (um alerta só)
    - FALHA, FALHA, OK, FALHA (nenhum alerta)
    - Duas sequências de 3 separadas por um OK (dois alertas)
    - Um evento inválido no meio de uma sequência (não zera)
    - Eventos digitados depois do FIM (não contam)

Permitido: while, break, True, False, if, elif, else, and, or, not, in,
input(), print(), str(), .upper(), .strip(), f-strings, tuplas, constantes,
contador = contador + 1 (como no while_infinito.py).
Proibido: for, def, try, continue, listas, +=. Ainda não chegamos lá.
"""
