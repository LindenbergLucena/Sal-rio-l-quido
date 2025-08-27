nome = input("Digite seu nome: ")
valorhora = float(input("Qual o valor recebido por hora trabalhada: "))
quanthora = float(input("Qual a quantidade de horas trabalhadas: "))
# Cálculos
salbruto = valorhora * quanthora
irpf = salbruto * 0.11
inss = salbruto * 0.09
sind = salbruto * 0.04
descontos = irpf + inss + sind
saliquido = salbruto - descontos
# Apresentação do resultados
print(f"Salário bruto: R$ {salbruto:.2f}")
print(f"Imposto de renda: R$ {irpf:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Sindicato: R$ {sind:.2f}")
print()
print(nome)
print(f"Seu salário líquido é: R$ {saliquido:.2f}")
