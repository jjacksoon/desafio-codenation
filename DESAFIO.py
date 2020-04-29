import string
def criptografia(frase, deslocamento):
    alpha = string.ascii_lowercase
    alpha_deslocado = alpha[deslocamento:] + alpha[:deslocamento]
    equivalencia = str.maketrans(alpha, alpha_deslocado)
    return frase.translate(equivalencia)

texto = str(input('Frase criptografada: ')).strip().lower()
print(f'Frase criptografada: {texto}')
print()
print(f'Frase descriptografada: {(criptografia(texto, -12))}')