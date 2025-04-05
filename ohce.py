def ohce(texto):
    resultado = texto[::-1]
    if texto == resultado:
        return f"{resultado}\n¡Bonita palabra!"
    return resultado
