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




    tamano=40 #quemado por ahora pero se deberia poner segun la pantalla
    espacio=int(tamano*0.10) 
    margen=50
    frame_h,frame_w,frame_c=frame.shape
    offset1=espacio + margen
    offset2=espacio + margen

    multTablero=10
    tableroSize=int(multTablero*tamano)
    multMargen=0.55
    tableroMarg=int(multMargen*margen)


    tablero=cv2.imread("tablero-negro.png")
    tablero=cv2.rotate(tablero, cv2.ROTATE_90_COUNTERCLOCKWISE)
    tablero=resize(tablero,width=tableroSize,height=tableroSize)
    tablero=cv2.cvtColor(tablero,cv2.COLOR_BGR2BGRA)

    overlay=np.zeros((frame_h,frame_w,4),dtype="uint8")
    tablero_h,tablero_w,tablero_c=tablero.shape

    for i in range(tablero_h):
        for j in range(tablero_w):
            if tablero[i,j][3]!=0:
                overlay[i+tableroMarg, j+tableroMarg]=tablero[i,j]
                        

    cv2.addWeighted(overlay,1,frame, 1 , 0, frame)



    for g in range(6):
        if (g % 2) != 0:
            offset2+=(espacio+tamano)

        for h in range(4):

            if g<3:

                fichaRoja=cv2.imread("Red.png")
                fichaR=resize(fichaRoja,width=tamano,height=tamano)
                FR=cv2.cvtColor(fichaR,cv2.COLOR_BGR2BGRA)

                overlay=np.zeros((frame_h,frame_w,4),dtype="uint8")
                FR_h,FR_w,FR_c=FR.shape

                for i in range(FR_h):
                    for j in range(FR_w):
                        if FR[i,j][3]!=0:
                            overlay[i+offset2, j+offset1]=FR[i,j]
                        

                cv2.addWeighted(overlay,1,frame, 1 , 0, frame)
            else:
                fichaRoja=cv2.imread("Black.png")
                fichaR=resize(fichaRoja,width=tamano,height=tamano)
                FR=cv2.cvtColor(fichaR,cv2.COLOR_BGR2BGRA)

                overlay=np.zeros((frame_h,frame_w,4),dtype="uint8")
                FR_h,FR_w,FR_c=FR.shape

                for i in range(FR_h):
                    for j in range(FR_w):
                        if FR[i,j][3]!=0:
                            overlay[i+offset2, j+offset1]=FR[i,j]
                        

                cv2.addWeighted(overlay,1,frame, 1 , 0, frame)


            if(h==3):
                offset2=espacio + margen
            else:
                offset2+=(2*tamano + 2*espacio)
        if(g==2):
            offset1+=(3*tamano + 3*espacio)
        else:
            offset1+=(tamano + espacio)


    cv2.imshow("Video: --> Original",frame)
    
    key = cv2.waitKey(33) #Retraso en milisegundos para leer el siguiente frame (nota para archivo de imagen poner 0 )
    #Termina presionando la tecla Esc
    if (key==27):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

capture.release()
