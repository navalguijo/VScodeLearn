# Decir Hola Mundo
print("Hola Mundo")

# Pedir el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")
# Lista de colores disponibles
colores_disponibles = {
    "rojo": "\033[91m",
    "verde": "\033[92m",
    "azul": "\033[94m",
    "amarillo": "\033[93m",
    "cian": "\033[96m",
    "magenta": "\033[95m"
}

# Mostrar opciones al usuario
print("Colores disponibles:")
for color in colores_disponibles:
    print(f"- {color}")

color = input("Elige un color de la lista para el texto: ")

# Imprimir mensaje personalizado en el color elegido
if color.lower() in colores_disponibles:
    print(colores_disponibles[color.lower()] + "Hola " + nombre + " \033[0m")
else:
    print("Color no reconocido, mostrando mensaje en color predeterminado.")
    print("Hola " + nombre)
    

