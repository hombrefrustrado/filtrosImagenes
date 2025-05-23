# Proyecto: Tratamiento de Imágenes

Este proyecto permite aplicar diversos filtros y transformaciones a imágenes utilizando Python y librerías científicas. Es un ejercicio práctico para el curso de Inteligencia Artificial.

## Requisitos

- Python 3.8 o superior
- Dependencias instalables con pip:
  - numpy
  - pillow
  - scipy

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

- `main.py`: Script principal para ejecutar la aplicación de tratamiento de imágenes.
- `TratamientoImagenes.py`: Funciones para procesar y transformar imágenes.
- `imagenes/`: Carpeta donde debes colocar las imágenes a editar y donde se guardarán los resultados.
- `requirements.txt`: Lista de dependencias necesarias.

## Uso

1. Coloca la imagen que deseas editar en la carpeta `imagenes/`.
2. Ejecuta el script principal:

   ```bash
   python main.py
   ```

3. Sigue las instrucciones en la consola para seleccionar la imagen y aplicar los filtros o transformaciones deseadas.
4. Puedes guardar la imagen editada en la misma carpeta `imagenes/`.

## Funcionalidades Disponibles

- Ajustar brillo y contraste
- Aplicar croma (eliminar un color específico)
- Desplazar imagen
- Invertir colores
- Convertir a escala de grises
- Aplicar desenfoque (con kernel personalizado)
- Rotar imagen (90, 180, 270 grados)
- Anular canales de color (R, G, B)
- Detección de bordes (filtros de Sobel)

## Contribuciones

Si deseas contribuir:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.