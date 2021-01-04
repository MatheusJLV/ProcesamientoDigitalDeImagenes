import cv2     #llama a OpenCv
#from Settings import WIDTH, HEIGHT #pip install python-settings
from imutils import resize
import numpy as np


def inputImg(message="\tPath de la imagen: "):   #función para cargar un archivo de imagen
    while (True):
        path = input (message)
        try:
            return cv2.imread(path, 1)
        except:
            print ("\n\tRuta invalida")

def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(y,x)


imgWelcome=cv2.imread("./Fotos_DIP_Proyecto/Welcome.jpg", 1)
imgComienzo=cv2.imread("./Fotos_DIP_Proyecto/Comenzar.jpg", 1)
imgSalir=cv2.imread("./Fotos_DIP_Proyecto/Salir.jpg", 1)

cv2.namedWindow("Checkers", cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('Checkers',draw_circle)

img=imgWelcome
cont=1
while(True):

    if cont==1:
        cv2.imshow("Checkers", imgComienzo)
    elif cont==2:
        cv2.imshow("Checkers", imgSalir)

    key = cv2.waitKey(33)
    if (key==27):
        break
    elif key==119:
        print('w')
        cont=1
    elif key==115:
        print('s')
        cont=2
    elif key==13:
        if cont==1:
            print("comenzar juego")
        elif cont==2:
            print("salir")
            break
    elif key==-1:  
        continue
    else :
        print(key)