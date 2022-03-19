def is_prime(n):
    # Função que retorna "True" se n for primo e "False" se não for
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True