nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
prioridade = "NÃO"

if idade >= 65:
    prioridade = "SIM"

print(f"O paciente  {nome} possui atendimento proritário? {prioridade}")