"""
TODO: Tratar erros com `Try/Except`
"""
RESPOSTAS_VALIDAS_DOENCA_INFECTOCONTAGIOSA = ("SIM", "NAO", "NÃO")

nome = input("Digite o nome: ").strip()
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? (SIM/NAO): ").upper().strip()

if (not nome or idade <= 0 or idade > 120) or (doenca_infectocontagiosa not in RESPOSTAS_VALIDAS_DOENCA_INFECTOCONTAGIOSA):
    print("""
-------------------------------------------------------------------------
DADOS INVÁLIDOS - Verifique se:
    - O nome foi digitado corretamente
    - Idade entre 1 e 120 anos
    - Responda a suspeita de doença infectocontagiosa com SIM ou NAO
-------------------------------------------------------------------------
""")

else:
    msg = f"O paciente {nome.upper()} será direcionado para sala"

    sala = "BRANCA"
    prioridade = "SEM prioridade"

    if doenca_infectocontagiosa == "SIM":
        sala = "AMARELA"
    if idade >= 65:
        prioridade = "COM prioridade"
    print(f"{msg} {sala} - {prioridade}")
