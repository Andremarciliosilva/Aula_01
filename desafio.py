
# Solicita ao usuário que dige seu nome

usuario = input("Digite o seu nome:")

# Solicita ao usuário que digite o valor do seu salário e converte a entrada pra um número de ponto flutuante

valor_salario = input("Digite o valor do seu salário:")

valor_salario_float = float(valor_salario)

# Solicita ao usuário que digite o valor do bônus recebido e converte a entrada para um número de ponto flutuante.

valor_bonus = input("Digite o valor do bônus:")

valor_bonus_float = float(valor_bonus)

# Cálculo do valor do bônus final (Bonus constante = 1000)

bonus_constante = float(1000)

bonus_final = bonus_constante + valor_salario_float * valor_bonus_float

print(f"O valor do bônus final do {usuario} é de: {bonus_final}")
