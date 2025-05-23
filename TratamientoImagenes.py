import os
from PIL import Image
import numpy as np
from scipy.ndimage import convolve
from scipy.signal import convolve2d


# Cada #### se corresponde con una acción que se puede realizar con una única línea de código

# Ajustar brillo. Positivo => más brillo, negativo => menos brillo
def ajustar_brillo(imagen_array, valor_brillo):
    return np.clip(imagen_array+np.array([valor_brillo,valor_brillo,valor_brillo]),0,255).astype(np.uint8)
# Ajustar contraste
def ajustar_contraste(imagen_array, factor_contraste):
    return np.clip(imagen_array*factor_contraste,0,255).astype(np.uint8)

def aplicar_croma(imagen_array, color_croma):
    mascara = np.all(imagen_array == color_croma, axis=-1)
    imagen_rgba = np.dstack((imagen_array, 255 * np.ones(imagen_array.shape[:2], dtype=np.uint8)))
    
    imagen_rgba[mascara,3] = 0
    
    return imagen_rgba.astype(np.uint8)

# Desplazar imagen
def desplazar_imagen(imagen_array, desplazamiento_x, desplazamiento_y):
    #### Creamos un array de tamaño igual al de la imagen con todos los valores a cero
    #### En dicho array asignamos los valores de la imagen original, pero desplazados según los parámetros
    alto, ancho, canales = imagen_array.shape
    imagen_desplazada = np.zeros((alto+desplazamiento_y,ancho+desplazamiento_x,canales),dtype=np.uint8)
    imagen_desplazada[desplazamiento_y:,desplazamiento_x:]=imagen_array[:,:]
    return imagen_desplazada.astype(np.uint8)


# Invertir colores
def invertir_colores(imagen_array):
    return np.clip(np.array([255,255,255])-imagen_array,0,255).astype(np.uint8)

# Convertir a escala de grises
def convertir_a_gris(imagen_array):
    imagen_gris=imagen_array[:,:,0]*0.2989+imagen_array[:,:,1]*0.5870+imagen_array[:,:,2]*0.1140
    return imagen_gris.astype(np.uint8)

def otro_gris(imagen_array):
    imagen_gris = np.mean(imagen_array, axis=2)
    return imagen_gris.astype(np.uint8)

def aplicar_desenfoque(imagen_array, tamano_kernel=5):
    kernel = np.ones((tamano_kernel, tamano_kernel)) / (tamano_kernel ** 2)
    imagen_desenfocada = np.zeros_like(imagen_array)
    for i in range(3):  # Aplicar a cada canal (R, G, B)
        imagen_desenfocada[:,:,i] = convolve(imagen_array[:,:,i],kernel)
    return imagen_desenfocada.astype(np.uint8)

# Rotar imagen
def rotar_imagen(imagen_array, angulo=90):
    imagen_aux=np.zeros_like(imagen_array)
    if angulo == 90:
        imagen_aux=np.rot90(imagen_array,1)
    elif angulo == 180:
        imagen_aux=np.rot90(imagen_array,2)
    elif angulo == 270:
        imagen_aux=np.rot90(imagen_array,3)
    else:
        raise ValueError("Ángulo de rotación no válido. Use 90, 180 o 270.")
    return imagen_aux.astype(np.uint8)

# Anular canal. 0=R, 1=G, 2=B
def anular_canal(imagen_array, numCanal):
    imagen_sincanal = np.copy(imagen_array)
    imagen_sincanal[:,:,numCanal]=0
    return imagen_sincanal.astype(np.uint8)

# Detección de bordes con convolución aplicando filtros de Sobel
def detectar_bordes(imagen_array):
    
    # Convertir a gris
    if len(imagen_array.shape) == 3:
        imagen_gris = convertir_a_gris(imagen_array)
    else:
        imagen_gris = imagen_array
    # Definir los kernels de Sobel para detección de bordes
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])  # Detecta bordes verticales
    sobel_y = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ])  # Detecta bordes horizontales
    # Aplicar las convoluciones para detectar bordes en las direcciones X e Y
    # Same mantiene el tamaño del resultado
    # symm refleja valores cercanos en bordes para convolucionar en límites de la imagen
    #### Calculamos bordes_x con convolve2d
    #### Calculamos bordes_y con convolve2d
    #### Calculamos magnitud del gradiente
    #### Normalizamos los bordes al rango [0, 255]
    # Convertir a tipo uint8

    bordes_x = convolve2d(imagen_gris,sobel_x,mode='same',boundary='symm')
    bordes_y = convolve2d(imagen_gris,sobel_y,mode='same',boundary='symm')
    magnitud = np.sqrt(bordes_x**2 + bordes_y**2)
    
    magnitud = (magnitud / np.max(magnitud)) * 255
    bordes = magnitud.astype(np.uint8)


    return bordes