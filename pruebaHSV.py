import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
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


    cv2.imshow("Frame", frame)
    #cv2.imshow("Blue", blue_mask) SOLO PARA VER
    #cv2.imshow("Green", green_mask) SOLO PARA VER

    #YA NO USAR
    #cv2.imshow("Red", red)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    #cv2.imshow("Result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break