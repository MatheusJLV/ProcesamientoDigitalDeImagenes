'''
    PROCESAMIENTO DIGITAL DE IMÁGENES

    MANEJO DE IMÁGENES EN OPENCV CON PHYTON
'''
import math
import numpy as np
import cv2

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
        
        
# Driver code     
s = ['Geeks', 'for', 'Geeks'] 
print(listToString(s)) 

def inputImg(message="\tPath de la imagen: "):   #función para cargar un archivo de imagen
    while (True):
        path = input (message)
        try:
            return cv2.imread(path, 1)
        except:
            print ("\n\tRuta invalida")

print ("\n\t\tLABORATORIO 3\n\tMANEJO DE IMÁGENES EN OPENCV")

while(True):
    print ("\n\n\t0. Salir\n\t1. Cargar una imagen\n\t2. Clonar una imagen"+
           "\n\t3. Selección de un ROI\n\t4. Convertir RGB a Gray Level"+
           "\n\t5. Valor de un Pixel en su posición fila y columna (brillo)\n\t6. Inicializar una imagen"+
           " con valor constante\n\t7. Obtener valor de nivel de brillo"
           " para una posición (i,j) dada\n\t8. Extraer canales"+
           " RGB de una imagen\n\t9. Realzado de brillo de una imagen\n\t10. Separar imagenes\n\t11. Unir imagenes\n")
    op = input("\n\tIngrese la opcion --> ")

    if (op=='0'):
        break
    elif (op=='10'):
        print ("\n\tCargar una imagen desde un archivo\n")
        img = inputImg()

        cv2.namedWindow("VentanaROI", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("VentanaROI", img)
        r = cv2.selectROI(img)
        roi = img[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
        cv2.imshow("VentanaROI", roi)
        cv2.waitKey(0)

        img=roi

        cv2.imshow("Imagen", img)
        cv2.waitKey(0)
        print("Tamaño de imagen(ancho, largo, canales)")
        print(img.shape)
        largo=img.shape[0]
        ancho=img.shape[1]
        b, g, r = cv2.split(img)
        colores=[]
        color=[]
        for i in range(largo):
        	for j in range(ancho):
        		color.append(b[i][j])
        		color.append(g[i][j])
        		color.append(r[i][j])
        		if not(color in colores):
        			colores.append(color)
        		color=[]
        print("colores")
        print(colores)
        #for k in range(4):
        #minimo y maximo
        umbral=[[255,0],[255,0],[255,0]]
        for h in range(len(colores)):
        	print(colores[h])
        	for g in range(3):
	        	if (umbral[g][0]>colores[h][g]):
		        	umbral[g][0]=colores[h][g]
		        if (umbral[g][1]<colores[h][g]):
		        	umbral[g][1]=colores[h][g]

        print(umbral)




    elif (op=='11'):
        print ("\n\tUnir imagenes\n")
        img1 = cv2.imread("img1.bmp", 1)
        cv2.imshow("Imagen", img1)
        img2 = cv2.imread("img2.bmp", 1)
        cv2.imshow("Imagen2", img2)
        img3 = cv2.imread("img3.bmp", 1)
        cv2.imshow("Imagen3", img3)

        img4= img1+img2+img3
        cv2.imshow("Resultado", img4)

        cv2.waitKey(0)
        


    elif (op=='1'):
        print ("\n\tCargar una imagen desde un archivo\n")
        img = inputImg()
        cv2.imshow("Imagen", img)
        cv2.waitKey(0)
        
        
    elif (op=='2'):
        print ("\n\tClonar una imagen\n")
        img = inputImg()
        clon = img.copy()
        cv2.imshow("Imagen", img)
        cv2.imshow("Copia", clon)
        cv2.waitKey(0)
        
    elif (op=='3'):
        print ("\n\tSelección de un ROI\n")
        img = inputImg()
        cv2.namedWindow("Ventana", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Ventana", img)
        r = cv2.selectROI(img)
        roi = img[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
        cv2.imshow("Ventana", roi)
        cv2.waitKey(0)
        
    elif (op=='4'):
        print ("\n\tConvertir RGB a Gray Level\n")
        img = inputImg()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Imagen", img)
        cv2.imshow("Escala de grises", gray)
        cv2.waitKey(0)
        
    elif (op=='5'):
        print ("\n\tValor de un Pixel en su posición fila y columna\n")
        img = inputImg()
        cv2.imshow("Imagen", img)
        cv2.waitKey(0)
        coord = input ("\n\tIngrese coordenadas posición i,j: ")
        try:
            coord = coord.split(",")
            i = int(coord[0])
            j = int(coord[1])
            #Obtener el arreglo b,g,r de la coordenada
            pixel = img[i,j]
            print ("\n\tR: "+str(pixel[2])+" G: "+str(pixel[1])+" B: "+str(pixel[0]))
        except:
            print ("\n\tCoordenada invalida\n")
            
    elif (op=='6'):
        print ("\n\tInicializar imagen con un valor constante\n")
        ancho = input ("\n\tAncho de imagen: ")
        alto = input ("\n\tAlto de imagen: ")
        color = input ("\n\tColor r,g,b: ")
        try:
            color = color.split(",")
            #Inicializar canales con ceros
            r = np.zeros((int(alto),int(ancho)), dtype='uint8')
            g = np.zeros((int(alto),int(ancho)), dtype='uint8')
            b = np.zeros((int(alto),int(ancho)), dtype='uint8')
            #Asignar el valor fijo a todos los pixeles de cada canal
            r = r + int(color[0])
            g = g + int(color[1])
            b = b + int(color[2])
            #Agrupar canales rgb en una sola imagen
            img = cv2.merge((b,g,r))

            cv2.imshow("Imagen", img)
            cv2.waitKey(0)
        except:
            print ("\n\tDatos inválidos")
            
    elif (op=='7'):
        print ("\n\tObtener valor de gris\n")
        img = inputImg()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Imagen", gray)
        cv2.waitKey(0)
        coord = input ("\n\tIngrese coordenadas i,j: ")
        try:
            coord = coord.split(",")
            i = int(coord[0])
            j = int(coord[1])
            #Obtener el arreglo b,g,r de la coordenada
            pixel = gray[i,j]
            print ("\n\tNivel de brillo: "+str(pixel))
        except:
            print ("\n\tCoordenada invalida\n")
            
    elif (op=='8'):
        print ("\n\tExtraer canales RGB de una imagen\n")
        img = inputImg()
        cv2.namedWindow("Imagen", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Imagen", img)
        cv2.waitKey(0)
        b, g, r = cv2.split(img)
        cv2.setWindowTitle("Imagen", "Canal R")
        cv2.imshow("Imagen", r)
        cv2.waitKey(0)
        cv2.setWindowTitle("Imagen", "Canal G")
        cv2.imshow("Imagen", g)
        cv2.waitKey(0)
        cv2.setWindowTitle("Imagen", "Canal B")
        cv2.imshow("Imagen", b)
        cv2.waitKey(0)
        
    elif (op=='9'):
        print ("\n\tRealzado de brillo de un ROI\n")
        img1 = inputImg("\tRuta de imagen a realzar: ")
        img2 = inputImg("\tRuta imagen roi: ")
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow("Img1", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow("Img2", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Img1", img1)
        cv2.imshow("Img2", img2)
        cv2.waitKey(0)

        #Extracción del roi de la imagen 2
        img1 = cv2.add(img1, 20)
        img3 = cv2.bitwise_and(img1, img2)
        
        cv2.imshow("Img1", img3)
        cv2.setWindowTitle("Img1", "Img3")
        cv2.waitKey(0)

        #Reduccion de brillo de la imagen
        img1 = cv2.subtract(img1, 100)
        
        cv2.imshow("Img2", img1)
        cv2.setWindowTitle("Img2", "Img4")
        cv2.waitKey(0)

        #Suma del roi extraido y la imagen
        img3 = cv2.add(img1, img3)
        
        cv2.imshow("Img1", img3)
        cv2.setWindowTitle("Img1", "Roi Realzado")
        cv2.waitKey(0)
        
    else:
        print ("\n\tLa opción no es válida.")
        

    cv2.destroyAllWindows()



        
