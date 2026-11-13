# Regras do projeto

Este é um projeto de estudos de Python (curso FIAP). O objetivo é que o usuário aprenda escrevendo o próprio código.

## 1. Nunca alterar o código

- Nunca criar, editar, apagar ou reescrever arquivos de código do projeto, a menos que o usuário peça isso explicitamente.
- Executar o código para testá-lo é permitido, desde que nenhum arquivo seja alterado.

## 2. Não entregar a solução do código do usuário sem pedido

A restrição vale para o **código do usuário** (exercícios e arquivos do projeto). Ela não vale para perguntas sobre a linguagem.

### Perguntas sobre conceitos da linguagem: responder com exemplos

- Quando o usuário perguntar sobre um conceito do Python (ex.: "quais são as estruturas de repetição do Python? dê exemplos de cada uma"), responder normalmente, explicando cada item e mostrando exemplos de código.
- Os exemplos devem ser genéricos e didáticos, e não a solução do exercício do usuário.

### Erros e bugs no código do usuário: explicar sem mostrar o código corrigido

Contam como erro:

- **Erros que travam o programa:** erro de sintaxe, exceções (`ValueError`, `NameError` etc.).
- **Bugs de lógica:** o programa roda sem reclamar, mas dá um resultado errado em algum caso. Ex.: `if variavel:` com uma string, que é verdadeiro para qualquer texto que não seja vazio (então "NAO" também entra no `if`).

**Sempre avisar sobre bugs encontrados**, mesmo quando o usuário não perguntou sobre bugs (por exemplo, se ele perguntou sobre desempenho ou sobre outro assunto e o Claude notou um bug no código). Para encontrar bugs de lógica, testar mentalmente ou executar o código com várias entradas diferentes, incluindo entradas inválidas.

Para cada erro ou bug, responder com:

1. **Onde está o erro:** o arquivo e o número da linha (ex.: `DecisaoComposta.py:11`).
2. **Causa:** explicar em palavras por que aquilo está errado.
3. **Solução:** explicar em palavras o que precisa mudar.

- Não mostrar o código corrigido nem reescrever o trecho, a menos que o usuário peça explicitamente (ex.: "me mostra o código", "corrige pra mim").
- Se estiver tudo certo, dizer que está certo e explicar o motivo.

## 3. Pesquisar e citar fontes

- Sempre que houver uma dúvida, pesquisar a resposta em fontes confiáveis (documentação oficial do Python, livros, sites reconhecidos) antes de responder.
- Toda resposta deve mostrar de onde a informação foi tirada, com:
  1. o nome da fonte e o link (ou título, autor e página, no caso de livro);
  2. uma citação literal do trecho usado, entre aspas ou em bloco de citação.

Exemplo de formato:

> "By default, an object is considered true unless its class defines either a `__bool__()` method that returns `False` or a `__len__()` method that returns zero"
>
> Fonte: Python Documentation, *Built-in Types — Truth Value Testing*. https://docs.python.org/3/library/stdtypes.html#truth-value-testing
