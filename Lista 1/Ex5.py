def is_palindrome(word):
    # Função que verifica se a string "word" é um palíndromo
    if word == word[::-1]:
        return True
    return False


word = str(input())
if is_palindrome(word) == True:
    print(word, "é um palíndromo")
else:
    print(word, "não é um palíndromo")
