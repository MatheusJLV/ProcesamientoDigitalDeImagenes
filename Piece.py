
import cv2
from imutils import resize
import numpy as np

class Piece:

    def __init__(self, row, col, color, overlay, size):
        self.row = row
        self.col = col
        self.color = color
        self.overlay = overlay
        self.size = size
        self.king = False

        if self.color == "Red" :
            self.direction = 1
        else :
            self.direction = -1

    def changePos(self,row,col):
        self.row=row
        self.col=col
        

    def makeKing(self):
        self.king=True
        self.overlay[self.row:self.row+self.size,self.col:self.col+self.size]=0
        ficha=None
        if self.color == "Red" :
            ficha=cv2.imread("RedQ.png")
        else :
            ficha=cv2.imread("BlackQ.png")
        
        fichaR=resize(ficha,width=self.size,height=self.size)
        FR=cv2.cvtColor(fichaR,cv2.COLOR_BGR2BGRA)

        frame_h,frame_w,frame_c=self.overlay.shape

        overlay=np.zeros((frame_h,frame_w,4),dtype="uint8")
        FR_h,FR_w,FR_c=FR.shape

        for i in range(FR_h):
            for j in range(FR_w):
                if FR[i,j][3]!=0:
                    overlay[i+self.row, j+self.col]=FR[i,j]
        self.overlay=overlay




