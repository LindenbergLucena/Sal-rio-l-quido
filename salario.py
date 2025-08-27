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
print("Salário bruto: R$",salbruto)
print("Imposto de renda: R$",irpf)
print("INSS: R$", inss)
print("Sindicato: R$",sind)
print(nome,"seu salário líquido é: R$",saliquido)
