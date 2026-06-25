# Juego del Ahorcado 
# Estudiante: Mark Anthony Peña Velasco

palabra_secreta = "INGENIERIA"
longitud = len(palabra_secreta)

palabra_oculta = ["_"] * longitud
intentos = 6
letras_usadas = []

print("=== JUEGO DEL AHORCADO ===")
print(f"La palabra tiene {longitud} letras. Tienes {intentos} intentos.\n")

while intentos > 0 and "_" in palabra_oculta:
    print("Palabra:", " ".join(palabra_oculta))
    print(f"Letras ya probadas: {letras_usadas}")
    print(f"Intentos restantes: {intentos}\n")

    letra = input("Escribe una letra: ").upper()

    if len(letra) != 1 or not letra.isalpha():
        print("❌ Pon solo una letra válida\n")
        continue

    if letra in letras_usadas:
        print("⚠️ Ya probaste esa letra\n")
        continue

    letras_usadas.append(letra)

    if letra in palabra_secreta:
        print("✅ ¡Bien! La letra está\n")
        # La ponemos en su lugar
        for posicion in range(longitud):
            if palabra_secreta[posicion] == letra:
                palabra_oculta[posicion] = letra
    else:
        intentos = intentos - 1
        print("❌ Incorrecto\n")

if "_" not in palabra_oculta:
    print(f"🎉 ¡GANASTE! La palabra era: {palabra_secreta}")
else:
    print(f"💀 PERDISTE. La palabra era: {palabra_secreta}")