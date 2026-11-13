# python-fiap

Repositório de estudos de Python do curso da FIAP. Cada pasta `CapituloN-Tema`
acompanha um capítulo do curso.

## Estrutura

| Pasta | Origem | Conteúdo |
| --- | --- | --- |
| `Capitulo2-Variaveis/` | Apostila da FIAP | Variáveis e tipos |
| `Capitulo2-Decisoes/` | Apostila da FIAP | Estruturas de decisão (`if`/`elif`/`else`) |
| `Capitulo2-Forja-da-ATIKA/` | **Não é da FIAP** | Exercícios extras criados pelo Claude (modo ATIKA) |

## Capitulo2-Forja-da-ATIKA

Exercícios extras, com tema de segurança da informação, criados pelo Claude
para praticar o conteúdo do capítulo 2. **Eles não fazem parte da apostila da
FIAP.** Cada exercício usa somente o que já foi visto no curso até o capítulo
(nada de laços, funções ou `try`).

| Exercício | Arquivo | Situação |
| --- | --- | --- |
| 1. Política de senha | `PoliticaSenha.py` | Concluído |
| 2. Classificador de portas de rede | `ClassificadorPorta.py` | Concluído (refatoração pendente) |
| 3. Bloqueio de login e alerta de acesso suspeito | `BloqueioLogin.py` | A fazer |

### Testes

Cada exercício tem um script de teste em `Capitulo2-Forja-da-ATIKA/testes/`:

```bash
bash Capitulo2-Forja-da-ATIKA/testes/roda_todos.sh               # todos
bash Capitulo2-Forja-da-ATIKA/testes/testa_classificador_porta.sh  # só um
```

## TODO: refatoração no fim do curso

Cada exercício tem um comentário `TODO` logo abaixo do enunciado. O combinado:

- As soluções ficam como estão hoje, escritas só com o que eu sabia na época.
- Ao final do curso, vou refatorar **todos** os exercícios usando todo o
  conhecimento adquirido.
- O objetivo é comparar a versão antiga com a nova e medir o quanto meu nível
  evoluiu.

Para achar todos os pontos pendentes:

```bash
grep -rn "TODO" --include="*.py" .
```
