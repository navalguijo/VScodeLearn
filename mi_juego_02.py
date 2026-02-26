# vamos a comenzar cargando una imagen y mostrándola en pantalla
from PIL import Image
import matplotlib.pyplot as plt
# Cargar la imagen que esta en la carpeta graficos
imagen = Image.open("graficos/freepik__enhance__3918.jpg")
# Mostrar la imagen en pantalla
plt.imshow(imagen)
plt.axis("off") # para ocultar los ejes
plt.show()
