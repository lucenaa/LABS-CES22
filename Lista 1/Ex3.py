def sum_to(n):
    # Função que retorna a soma de todos os inteiros de 1 até n
    sum = 0
    for i in range(n):
        sum = sum + i + 1
    return sum


resultado = sum_to(10)
print(resultado)
