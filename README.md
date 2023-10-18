# Filtros CV
El objetivo del laboratorio era realizar 2 filtros tipo Instagram. El primer filtro se creó a partir de las herramientas de OpenCV y el segundo se programó tomando de base dicha librería pero haciendo todos los procesos.

**ADVERTENCIA**: para correr *tarea_3.py* puede que sea necesario tener Cython en el dispositivo

## Autores: 
- Cruz del Cid [CruzdelCid](https://github.com/CruzdelCid)
- Daniel Behar [dan-behar](https://github.com/dan-behar)

## Directorios
* imagenes: carpeta con 2 imágenes para probar los filtros
* videos: video usado para probar los filtros. El video utilizado fue grabado por Stefano Rinaldo y cargado a [Pexels](https://www.pexels.com/es-es/video/imagenes-de-drones-de-la-cima-de-la-montana-2871916/)
* Pruebas.ipynb: jupyter notebook donde se probaron los filtros previo a establecerlos en un archivo.py
* cvlib.py: archivo .py que contiene varias funciones usadas para visualizar los cambios en las imágenes
* external.c: filtro armado en Cython compilado para ser ejecutado con tarea_3.py
* external.html: archivo generado al compilar el proyecto en Cython
* external.pyx: archivo generado al compilar el proyecto en Cythonç
* laboratorio2.pdf: las instrucciones del ejercicio realizado
* setup.py: archivo generado al compilar el proyecto en Cython
* tarea_1.py: implementación del filtro **pencil**. Se utilizaron liberías de OpenCV
* tarea_2.py: implementación del filtro **sharpen** tratando de emular lo que OpenCV realiza en su función
* tarea_3.py: el filtro sharpen, armado en tarea_2.py, pero ahora ejecutado con Cython. El objetivo era aprovechar la mejora que Cython ofrece y ver qué tanto mejoraba la implementación entre ambas formas de armado
* video.py: archivo para poder capturar video desde una cámara web en la computadora

## Speedup
Parte del objetivo era calcular el Speedup entre la implementación de tarea_2.py y tarea_3.py
Calculo del speedup:

              
SpeedUp = t sharp / (t fast - sharp)

SpeedUp = 473 / 11
        = 43 

Para calcular el speedup tomamos el tiempo total en que el script 1 y el script 2 tardaron cada uno en procesar todo el video 
mountain.mp4, contenido la carpetas videos.
