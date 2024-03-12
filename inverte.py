def inverte_string(string):
    invertida_string = ""
    for i in range(len(string) - 1, - 1, -1):
        invertida_string += string[i]
    return invertida_string

# Exemplo de uso:
string_original = input("Digite uma string: ")
string_invertida = inverte_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
