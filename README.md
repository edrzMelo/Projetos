⚡ Calculadora de Consumo de Energia

📌 Sobre o projeto

A Calculadora de Consumo de Energia é uma programação desenvolvida em python que permite calcular o consumo mensal estimado de energia elétrica de um aparelho. O usuário informa o nome do aparelho, sua potência em watts (W) e o tempo médio de utilização por dia. Com essas informações, o programa calcula o consumo estimado em kWh por mês e o seu valor estimado mensal. OBS: A estimativa está sendo considerada com base no valor de R$ 0,75 por kWh.

🎯 Objetivo O objetivo do projeto é ajudar o usuário a entender quanto um aparelho pode consumir de energia elétrica durante um mês, utilizando informações simples sobre sua utilização.

🧮 Forma de calculo utilizado: O consumo mensal é calculado utilizando a seguinte fórmula: consumoMensal = (potencia * horasDia * 30) / 1000

Para calcular o custo estimado: custoEstimado = consumoMensal * 0.75

💻 Como executar este sistema

Pré-requisito É necessário ter o Python 3 instalado no computador.
Abrir o projeto Abra a pasta consumo-energia no Visual Studio Code.
Executar o programa Abra o terminal do VS Code e execute: python app.py
Informar os seguintes dados Nome do aparelho Potência em watts (W) Tempo médio de uso diário em horas Depois, o sistema mostrará o consumo mensal estimado e o custo aproximado.
📊 Exemplo de execução Digite o nome do aparelho: Geladeira Digite a potência do aparelho em watts (W): 100 Digite o tempo médio de uso diário em horas: 15

📊 Resultado: Aparelho: Geladeira Consumo estimado: 45.00 kWh/mês Custo estimado: R$ 33.75 por mês
