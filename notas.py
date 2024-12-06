# Inicializa o total e o contador de notas
total = 0
contador_notas = 0

# Loop para ler 10 notas
while contador_notas < 10:
    try:
        # Solicita a entrada da nota
        nota = float(input("Digite a nota: "))
        
        # Verifica se a nota é válida (por exemplo, entre 0 e 10)
        if 0 <= nota <= 10:
            total += nota
            contador_notas += 1
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

# Calcula a média
media = total / 10

# Imprime a média
print(f"A média da disciplina é: {media:.2f}")
