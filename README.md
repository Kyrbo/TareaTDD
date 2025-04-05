
Este programa simula la kata "Ohce", y está desarrollado aplicando TDD (Test Driven Development).

El funcionamiento es el siguiente:

1. Al iniciar, el programa solicita el nombre del usuario.
2. Según la hora actual, muestra un saludo personalizado:
   - Entre 06:00 y 11:59 → "¡Buenos días, [nombre]!"
   - Entre 12:00 y 19:59 → "¡Buenas tardes, [nombre]!"
   - Entre 20:00 y 05:59 → "¡Buenas noches, [nombre]!"
3. Luego, espera que el usuario escriba una palabra.
   - Si la palabra es "Stop!", el programa muestra "Adiós" y finaliza.
   - Si la palabra es un palíndromo (se lee igual al revés), la muestra invertida y agrega "¡Bonita palabra!".
   - En otros casos, simplemente invierte y muestra la palabra.
