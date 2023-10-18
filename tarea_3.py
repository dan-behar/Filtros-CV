"""
Calculo del speedup:

              t sharp
SpeedUp = ----------------
            t fast - sharp

SpeedUp = 473 / 11
        = 43 

Para calcular el speedup tomamos el tiempo total en que el escrip 1 y el script 2 se tardaron en procesar todo el video 
mountain.mp4, contenido la carpetas videos.
"""


from video import CountsPerSec, VideoCaptureThread, ImShowThread
import cv2 as cv
import numpy as np
import datetime
from external import sharpener_cy
import warnings
warnings.filterwarnings('ignore')


def sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv.filter2D(img, -1, kernel)
    return img_sharpen


def img_annotate(img, text, color=(0, 255, 0)):
    """ Annotate an image with text
    """
    img = np.array(sharpener_cy(img))
    # img = sharpen(img)

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

def threadBoth(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoCaptureThread(source).start()
    video_shower = ImShowThread(video_getter.frame,'CAPTURE AND WINDOW THREAD').start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
        video_shower.frame = frame
        cps.increment()




if __name__ == '__main__':

    # filename = "videos/mountain.mp4"
    # src = filename

    start_time = datetime.datetime.now()

    src = 0
    
    noThreading(src)
    #threadBoth(src)

    end_time = datetime.datetime.now()


    print("\n\nStart Time: ",start_time)
    print("End Time: ", end_time)
    print("Diff Time:", (end_time - start_time).seconds, "seconds")

    #captureThread(src)
    #windowThread(src)
    


