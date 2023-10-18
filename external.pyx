import cython
import numpy as np
@cython.boundscheck(False)
cpdef unsigned char[:, :, :] sharpener_cy(unsigned char[:, :, :] img):
    cdef int f, c, capas, capa, i, j, k_f, k_c
    cdef double pixel
    cdef double[:, :] kernel
    cdef unsigned char[:,:,:] sharp_img

    kernel = np.array([[-1, -1, -1], 
                        [-1, 9.5, -1], 
                        [-1, -1, -1]])
    
    # obtencion de dimensiones
    f = img.shape[0]
    c = img.shape[1]
    capas = img.shape[2]

    k_f = kernel.shape[0]
    k_c = kernel.shape[1]

    # Creación de imagen con ceros 
    sharp_img  = np.zeros((f, c, capas), dtype=np.uint8)

    # Aplicación del kernel
    for capa in range(capas): # Iteración capas
        for i in range(1, f-1): # Iteracion de filas 
            for j in range(1, c - 1): # Iteracion columnas
                matriz = img[i-1:i+2, j-1:j+2, capa] # Corte de la matriz 
                
                # matriz = np.multiply(matriz, kernel) # Calculo del kernel 
                # pixel = matriz.sum() # Suma del pixel 

                pixel = 0.0

                for fila in range(k_f): 
                    for columna in range(k_c): 
                        pixel += matriz[fila, columna] * kernel[fila, columna]

                if pixel < 0.0: 
                    pixel = 0.0
                elif pixel > 255.0: 
                    pixel = 255.0

                sharp_img[i, j, capa] = int(pixel) # se guardan en la sharp_img 

    return sharp_img