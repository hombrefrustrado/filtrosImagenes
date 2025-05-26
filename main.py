import os
import TratamientoImagenes as ti
import numpy as np
from PIL import Image

def cargarImagen(ruta:str,archivo:str):
    directorio = os.path.join(ruta,archivo)
    imagen = Image.open(directorio)
    imagen_array = np.array(imagen)
    imagen_array=imagen_array[:,:,:3]
    return imagen_array

def ponerArchivo():
    nombre = input("Indica con el siguiente formato nombre_del_archivo.extensión: ")
    ruta = os.path.join(os.getcwd(),"imagenes")
    return cargarImagen(ruta,nombre)

def guardarImagen(imagen):
    if imagen is not None:
        nombre_guardar = input("Introduce el nombre para guardar la imagen (incluye la extensión, por ejemplo: salida.png): ")
        ruta_guardar = os.path.join(os.getcwd(), "imagenes", nombre_guardar)
        if imagen.ndim == 2:
            Image.fromarray(imagen, 'L').save(ruta_guardar)
        else:
            Image.fromarray(imagen).save(ruta_guardar)
        print(f"Imagen guardada en {ruta_guardar}")
    else:
        print("No hay ninguna imagen editada para guardar.")
def limpiar_terminal():
  """Limpia la terminal.  Usa 'clear' en Linux/macOS y 'cls' en Windows."""
  if os.name == "posix":  # Linux/macOS
    os.system("clear")
  elif os.name == "nt":  # Windows
    os.system("cls")

print("Para usar la aplicación debes de meter un archivo en la carpeta imagenes y decir el nombre a continuación \n")
imagen = ponerArchivo()
print("Bienvenido al programa para tratamiento de imagenes")
imagen_editada = None
while(True):

    boton = int(
        input(
            "Pulsa uno de los siguientes botones para seleccionar una opción\n"
            "0 - Salir\n"
            "1 - Cambiar la imagen a editar\n"
            "2 - Guardar imagen\n"
            "3 - Aplicar filtro de gris\n"
            "4 - Ajustar brillo\n"
            "5 - Ajustar contraste\n"
            "6 - Aplicar croma\n"
            "7 - Desplazar imagen\n"
            "8 - Invertir colores\n"
            "9 - Convertir a gris\n"
            "10 - Aplicar desenfoque\n"
            "11 - Rotar imagen\n"
            "12 - Anular canal R\n"
            "13 - Anular canal G\n"
            "14 - Anular canal B\n"
            "15 - Detectar bordes\n"
            "16 - eliminar el color que quieras\n"
            "17 - desenfoque con kernel personalizado\n"
            "Boton: "
        )
    )
    print("\n")
    match boton:
        case 0:
            break
        case 1:
            imagen = ponerArchivo()
        case 2:
            guardarImagen(imagen_editada)
        case 3:
            imagen_editada = ti.convertir_a_gris(imagen)
            Image.fromarray(imagen_editada, 'L').show(title="Escala de Grises")
        case 4:
            valor = int(input("Introduce el valor de brillo a ajustar (ejemplo: 50): "))
            imagen_editada = ti.ajustar_brillo(imagen, valor)
            Image.fromarray(imagen_editada).show(title="Brillo Ajustado")
        case 5:
            valor = float(input("Introduce el factor de contraste (ejemplo: 1.5): "))
            imagen_editada = ti.ajustar_contraste(imagen, valor)
            Image.fromarray(imagen_editada).show(title="Contraste Ajustado")
            
        case 6:
            croma_img = np.array(Image.open(os.path.join(os.getcwd(), "imagenes", "croma.jpg")))
            imagen_editada = ti.aplicar_croma(croma_img, [0, 255, 1])
            Image.fromarray(imagen_editada, 'RGBA').show(title="Croma Aplicado")
        case 7:

            dx = int(input("Introduce el desplazamiento en X (ejemplo: 50): "))
            dy = int(input("Introduce el desplazamiento en Y (ejemplo: 30): "))
            imagen_editada = ti.desplazar_imagen(imagen, dx, dy)
            Image.fromarray(imagen_editada).show(title="Imagen Desplazada")
        case 8:
            imagen_editada = ti.invertir_colores(imagen)
            Image.fromarray(imagen_editada).show(title="Colores Invertidos")
        case 9:
            imagen_editada = ti.convertir_a_gris(imagen)
            Image.fromarray(imagen_editada, 'L').show(title="Escala de Grises")
        case 10:
            imagen_editada = ti.aplicar_desenfoque(imagen)
            Image.fromarray(imagen_editada).show(title="Imagen Desenfocada")
        case 11:
            angulo = int(input("Introduce el ángulo de rotación (ejemplo: 90): "))
            imagen_editada = ti.rotar_imagen(imagen, angulo=angulo)
            Image.fromarray(imagen_editada).show(title="Imagen Rotada")
        case 12:
            imagen_editada = ti.anular_canal(imagen, 0)
            Image.fromarray(imagen_editada).show(title="Imagen sin canal R")
        case 13:
            imagen_editada = ti.anular_canal(imagen, 1)
            Image.fromarray(imagen_editada).show(title="Imagen sin canal G")
        case 14:
            imagen_editada = ti.anular_canal(imagen, 2)
            Image.fromarray(imagen_editada).show(title="Imagen sin canal B")
        case 15:
            imagen_editada = ti.detectar_bordes(imagen)
            Image.fromarray(imagen_editada).show(title="Imagen (bordes)")
        case 16:
            r = int(input("Introduce el valor R del color a eliminar (ejemplo: 0): "))
            g = int(input("Introduce el valor G del color a eliminar (ejemplo: 255): "))
            b = int(input("Introduce el valor B del color a eliminar (ejemplo: 1): "))
            imagen_editada = ti.aplicar_croma(imagen, [r, g, b])
            Image.fromarray(imagen_editada, 'RGBA').show(title="Croma Aplicado")
        case 17:
            kernel = int(input("Introduzca el tamaño del kernel del desenfoque: "))
            imagen_editada=ti.aplicar_desenfoque(imagen,tamano_kernel=kernel)
        case _:
            print("boton no definido, pruebe de nuevo\n")
    limpiar_terminal()
