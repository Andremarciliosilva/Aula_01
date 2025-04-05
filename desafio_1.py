
# Solicita ao usuário que dige seu nome

while True:
    usuario = input("Digite o seu nome: ")
    
    if usuario.isalpha():
      break

    elif usuario.isdigit() == False:
        print("Por favor digite algum caracter.")

    else:
        print("Por favor digite apenas letras.")
 
# Solicita ao usuário que digite o valor do seu salário e converte a entrada pra um número de ponto flutuante

while True:
    valor_salario = input("Digite o valor do seu salário:")

    if valor_salario.isnumeric():
      break

    else:
        print("Por favor digite apenas números.")

valor_salario_int = int(valor_salario)
valor_salario_float = float(valor_salario_int)

# Solicita ao usuário que digite o valor do bônus recebido e converte a entrada para um número de ponto flutuante.

while True:
    valor_bonus = input("Digite o valor do bônus:")
    
    if valor_bonus.isnumeric():
      break

    else:
        print("Por favor digite apenas números.")

valor_bonus_int = int(valor_bonus)
valor_bonus_float = float(valor_bonus_int)

# Cálculo do valor do bônus final (Bonus constante = 1000)

bonus_constante = float(1000)

bonus_final = bonus_constante + valor_salario_float * valor_bonus_float

print(f"O valor do bônus final do {usuario} é de: R$ {bonus_final}")