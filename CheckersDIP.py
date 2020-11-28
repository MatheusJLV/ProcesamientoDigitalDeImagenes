'''
             PROCESAMIENTO DIGITAL DE IMÁGENES

               Como capturar video en OpenCv
    Captura de video desde una cámara o un archivo de video


En el presente laboratorio se aprenderá a capturar video desde una webcam o camara
de adquisicion, y se ofrece como alternativa cargar un archivo de video. Además se da  
a conocer las funciones de conversión de una imagen RGB a imagen Binaria o Escala de Grises.  
'''

import cv2     #llama a OpenCv
#from Settings import WIDTH, HEIGHT #pip install python-settings
from imutils import resize
import numpy as np


#Captura del archivo de video
#capture = cv2.VideoCapture("video1.avi")

#Captura de video desde cámara
capture = cv2.VideoCapture(0)


#Presentación de las diferentes imágenes y la señal de video
cv2.namedWindow("Video: --> Original", cv2.WINDOW_AUTOSIZE)
#Ventanas adicionales
#cv2.namedWindow("Video: --> escala de grises", cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow("Video: --> binarizado", cv2.WINDOW_AUTOSIZE)


while(True):

    #Lectura del frame desde la señal de video (cámara o archivo de video)
    ret, frame = capture.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    #Si llega al final del video no habrá frame
    if(not ret):
      break

    reinaNegra=cv2.imread("BlackQ.png")
    reinaN=resize(reinaNegra,width=50,height=50)
    RN=cv2.cvtColor(reinaNegra,cv2.COLOR_BGR2BGRA)

    frame_h,frame_w,frame_c=frame.shape
    overlay=np.zeros((frame_h,frame_w,4),dtype="uint8")
    RN_h,RN_w,RN_c=RN.shape

    for i in range(RN_h):
    	for j in range(RN_w):
    		if RN[i,j][3]!=0:
    			overlay[i+10,j+10]=RN[i,j]

    cv2.addWeighted(overlay,0.5,frame, 1 , 0, frame)

    #Convertir a escala de grises
    #frameGris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Convertir a binaria
    #ret, frameBin = cv2.threshold(frameGris, 170, 255, cv2.THRESH_BINARY)

    #Muestra el video resultante en su respectiva ventana
    cv2.imshow("Video: --> Original",frame)
    #cv2.imshow("Video: --> escala de grises",frameGris)
    #cv2.imshow("Video: --> binarizado",frameBin)

    key = cv2.waitKey(33) #Retraso en milisegundos para leer el siguiente frame (nota para archivo de imagen poner 0 )
    #Termina presionando la tecla Esc
    if (key==27):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

capture.release()
