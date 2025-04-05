from datetime import datetime

def ohce(texto):
    if texto == "Stop!":
        return "Adios"
    resultado = texto[::-1]
    if texto == resultado:
        return f"{resultado}\n¡Bonita palabra!"
    return resultado

def saludar(nombre, hora):
    if 6 <= hora < 12:
        return f"¡Buenos días, {nombre}!"
    elif 12 <= hora < 20:
        return f"¡Buenas tardes, {nombre}!"
    else:
        return f"¡Buenas noches, {nombre}!"

#Terimal interactuable

if __name__ == "__main__":
    
    nombre = input("¿Cómo te llamas? ")
    hora_actual = datetime.now().hour
    print(saludar(nombre, hora_actual))

    while True:
        entrada = input("> ")
        respuesta = ohce(entrada)
        print(respuesta)
        if entrada == "Stop!":
            break
