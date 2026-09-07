print("⚡ Calculadora de Consumo de Energia ⚡")
aparelho = input("Digite o nome do aparelho: ").strip() or "Aparelho não informado"
potencia = ler_numero("Digite a potência do aparelho em watts (W): ")
horasDia = ler_numero("Digite o tempo médio de uso diário em horas: ", 24)

consumoMensal = (potencia * horasDia * 30) / 1000

valorKwh = 0.75
custoEstimado = consumoMensal * valorKwh

print("\n📊 Resultado:")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custoEstimado:.2f} por mês")