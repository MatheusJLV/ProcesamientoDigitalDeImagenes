'''
             PROYECTO DE PROCESAMIENTO DIGITAL DE IMÁGENES

               JUEGO DE DAMAS POR VISION DE COMPUTADOR

 
'''

import cv2     #llama a OpenCv
#from Settings import WIDTH, HEIGHT #pip install python-settings
from imutils import resize
import numpy as np

#Captura de video desde cámara
capture = cv2.VideoCapture(0)


cv2.namedWindow("Video: --> Original", cv2.WINDOW_AUTOSIZE)



while(True):

    #Lectura del frame desde la señal de video (cámara o archivo de video)
    ret, frame = capture.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    if(not ret):
      break

    tamano=50 #quemado por ahora pero se deberia poner segun la pantalla
    espacio=tamano*0.15
    reinaNegra=cv2.imread("BlackQ.png")
    reinaN=resize(reinaNegra,width=tamano,height=tamano)
    RN=cv2.cvtColor(reinaNegra,cv2.COLOR_BGR2BGRA)

    frame_h,frame_w,frame_c=frame.shape
    overlay=np.zeros((frame_h,frame_w,4),dtype="uint8")
    RN_h,RN_w,RN_c=RN.shape

    for i in range(RN_h):
        for j in range(RN_w):
            if RN[i,j][3]!=0:
                overlay[i+10,j+10]=RN[i,j]

    cv2.addWeighted(overlay,0.5,frame, 1 , 0, frame)

    cv2.imshow("Video: --> Original",frame)
    
    key = cv2.waitKey(33) #Retraso en milisegundos para leer el siguiente frame (nota para archivo de imagen poner 0 )
    #Termina presionando la tecla Esc
    if (key==27):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

capture.release()
