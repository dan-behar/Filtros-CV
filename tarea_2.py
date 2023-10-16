from video import CountsPerSec, VideoCaptureThread, ImShowThread
import argparse
import cv2 as cv
import numpy as np
import cvlib


def sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv.filter2D(img, -1, kernel)
    return img_sharpen

def sharpener(img): 
    # Creación de imagen con ceros 
    dimensions = img.shape
    f, c, capas = (0, 0, 0)
    sharp_img  = np.zeros(dimensions, dtype=np.float64)

    # Verificamos si la imagen es a color
    is_color = False 

    if len(sharp_img.shape) == 3: 
        is_color = True
        f, c, capas = dimensions

    # Creación del kernel     
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])


    # Aplicación del kernel
    if is_color == True: 

        for capa in range(capas): # Iteración capas
 
            for i in range(1, f-1): # Iteracion de filas 

                for j in range(1, c - 1): # Iteracion columnas

                    matriz = img[i-1:i+2, j-1:j+2, capa] # Corte de la matriz 

                    matriz = np.multiply(matriz, kernel) # Calculo del kernel 

                    pixel = matriz.sum() # Suma del pixel 

                    sharp_img[i, j, capa] = pixel # se guardan en la sharp_img 


    # sharp_img = sharp_img.astype('uint8')
                    

    # print("Shape:", img.shape)

    # Transfomación a uint8
    # if is_color == True: 

    #     sharp_img = float64_to_uint8(sharp_img)
        
        # for capa in range(capas): # Iteración capas

        #     print(np.var(sharp_img[:, :, capa]))
            
        #     sharp_img[:, :, capa] = float64_to_uint8(sharp_img[:, :, capa])

        #     cvlib.imgview(sharp_img[:, :, capa])

    # sharp_img = cv.normalize(sharp_img, None, 0, 255, cv.NORM_MINMAX) 
    # sharp_img = cv.convertScaleAbs(sharp_img) 


    # # Trasnform 
    # if len(sharp_img.shape) == 3: 
    #     print("Dimensiones",sharp_img.shape)
    #     print("Image is color")

    #     for i in range(3): 
    #         print(sharp_img[:,:,i])

    #         sharp_img[:,:,i] = float64_to_uint8(sharp_img[:,:,i])

    #         print(sharp_img, "\n----")

    return sharp_img

def img_annotate(img, text, color=(0, 255, 0)):
    """ Annotate an image with text
    """

    img = sharpener(img)

    cv.putText(img, text,(10, 120), cv.FONT_HERSHEY_SIMPLEX, 3, color)
    return img


def noThreading(source=0):
    """No threading text
    """

    cap = cv.VideoCapture(source)
    cps = CountsPerSec().start()

    while True:
        ret, frame = cap.read()
        if not ret or cv.waitKey(1) == ord("q"):
            break
        
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
       
        cv.imshow("NO_THREAD", frame)
        cps.increment()

if __name__ == '__main__':

    # filename = "videos/maldives.mp4"
    # src = filename
    src = 0
    
    noThreading(src)

    #captureThread(src)
    #windowThread(src)
    #threadBoth(src)


# img = cv.imread("imagenes/panaderia.jpg",cv.IMREAD_COLOR) 
# img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# img = sharpen(img)
# cvlib.imgview(img)




