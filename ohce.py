def ohce(texto):
    if texto == "Stop!":
        return "Adios"
    resultado = texto[::-1]
    if texto == resultado:
        return f"{resultado}\n¡Bonita palabra!"
    return resultado

