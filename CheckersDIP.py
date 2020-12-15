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


cv2.namedWindow("Checkers", cv2.WINDOW_AUTOSIZE)

contador=0
tablero=[]
piezasBlancas=[]
piezasRojas=[]
while(True):

    #Lectura del frame desde la señal de video (cámara o archivo de video)
    ret, frame = capture.read()


    #lectura de puntero

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Red color
    #low_red = np.array([161, 50, 50])
    #high_red = np.array([179, 255, 255])
    #red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    #red = cv2.bitwise_and(frame, frame, mask=red_mask)


    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #deteccion de contornos

    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,[0,255,255],3)NO USAR ESTE, O SE DIBUJA TODOS LOS CHIQUITOS. ES DE MUESTRA
    for c in contours:
        area=cv2.contourArea(c)
        if (area > 50):
            M=cv2.moments(c)
            if(M["m00"]==0):M["m00"]=1
            x1=int(M["m10"]/M["m00"])
            y1=int(M["m01"]/M["m00"])
            cv2.circle(frame,(x1,y1),7,(0,255,255),-1)
            #PARA DIBUJAR CONTORNO Y MOSTRAR COORDENADAS. PERO NO NECESITA EXIBIRSE
            #font=cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(frame,"{} {}".format(x1,y1),(x1+10,y1),font,0.75,(0,255,255),1,cv2.LINE_AA)
            #nuevoContorno=cv2.convexHull(c)
            #cv2.drawContours(frame,[c],-1,[0,255,255],3)
            break


    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    #imagen,contornos,herarquia=cv2.findContours(green_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) PARA CV3, ESTAMOS EN EL 4
    
    #deteccion de contornos
    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,[255,0,255],3) NO USAR ESTE, O SE DIBUJA TODOS LOS CHIQUITOS. ES DE MUESTRA
    for c in contours:
        area=cv2.contourArea(c)
        if area > 50:
            M=cv2.moments(c)
            if(M["m00"]==0):M["m00"]=1
            x2=int(M["m10"]/M["m00"])
            y2=int(M["m01"]/M["m00"])
            cv2.circle(frame,(x2,y2),7,(255,0,255),-1)
            #PARA DIBUJAR CONTORNO Y MOSTRAR COORDENADAS. PERO NO NECESITA EXIBIRSE
            #font=cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(frame,"{} {}".format(x2,y2),(x2+10,y2),font,0.75,(255,0,255),1,cv2.LINE_AA)
            #nuevoContorno=cv2.convexHull(c)
            #cv2.drawContours(frame,[c],-1,[255,0,255],3)
            break
            
    #lectura de puntero




    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)

    if(not ret):
      break


    if(contador==0):
        contador=1

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
                        
        tablero=overlay
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
                            
                    piezasRojas.append(overlay)
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
                            
                    piezasBlancas.append(overlay)
                    cv2.addWeighted(overlay,1,frame, 1 , 0, frame)


                if(h==3):
                    offset2=espacio + margen
                else:
                    offset2+=(2*tamano + 2*espacio)
            if(g==2):
                offset1+=(3*tamano + 3*espacio)
            else:
                offset1+=(tamano + espacio)
    
    else :
        cv2.addWeighted(tablero,1,frame, 1 , 0, frame)
        for piezaB in piezasBlancas:
            cv2.addWeighted(piezaB,1,frame, 1 , 0, frame)

        for piezaR in piezasRojas:
            cv2.addWeighted(piezaR,1,frame, 1 , 0, frame)


    cv2.imshow("Checkers",frame)
    
    key = cv2.waitKey(33) #Retraso en milisegundos para leer el siguiente frame (nota para archivo de imagen poner 0 )
    #Termina presionando la tecla Esc
    if (key==27):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

capture.release()
