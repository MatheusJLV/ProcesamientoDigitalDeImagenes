import cv2

from OpcionMovimiento import Movimiento

class Board:

    def __init__(self, overlay,pieces, height, width, sizeSquare, space,estado):
        self.board= overlay
        self.size_square=sizeSquare
        self.height=height
        self.space=space
        self.width=width
        self.pieces= pieces
        self.selectedPiece=None
        self.red_left = self.black_left = 12
        self.red_kings = self.black_kings= 0
        self.opciones = []
        self.putPieces()
        self.turno = "Black"
        self.blocked= False
        self.ganador=""
        self.estado=estado
       
        
    def putPieces(self):

        for key in self.pieces:
            cv2.addWeighted(self.pieces[key].overlay,1,self.board, 1 , 0, self.board)

    def cambiarTurno(self):

        if self.turno == "Red":

            if self.black_left==0:
                print("GANO  RED")
                self.ganador="Red"
                self.estado["evento"]="final"
            else :
                self.turno = "Black"
                self.PosibleComer()


        elif self.turno == "Black":
            if self.red_left==0:
                print("GANO BLACK")
                self.ganador="Black"
                self.estado["evento"]="final"
            else :
                self.turno = "Red"
                self.PosibleComer()

    def PosibleComer(self):
        for key in self.pieces:
            piece= self.pieces[key]
            if piece.color==self.turno:
                self.planificarPieza(piece)
        cant=0
        opciones=[]
        for opcion in self.opciones:
            if len(opcion.piezas)>cant :
                opciones.clear()
                opciones.append(opcion)
                cant=len(opcion.piezas)
            elif len(opcion.piezas)==cant and cant!=0  :
                opciones.append(opcion)

        self.opciones=opciones
        self.dibujarOpciones()
        if len(opciones)>0:
            self.blocked=True

                


    def movePiece(self,opcion):

        rowIni= opcion.row
        colIni= opcion.col

        for piece in opcion.piezas:
            print(piece.row,piece.col)
            self.borrarPieza(piece)

        piece=opcion.pieza
        #piece=self.pieces[(self.selectedPiece)]
        #roi=self.board[piece.row: piece.row+piece.size,piece.col:piece.col+piece.size]
        

        if colIni>(self.width-self.size_square) and piece.color=="Red":
            piece.makeKing()
            
        elif colIni<(self.width-self.size_square*7) and piece.color=="Black":
            piece.makeKing()
            

        roi=piece.overlay[piece.row: piece.row+piece.size,piece.col:piece.col+piece.size]

        rowFinal=rowIni+piece.size
        colFinal=colIni+piece.size

        self.board[rowIni:rowFinal,colIni:colFinal]=roi
        self.board[piece.row: piece.row+piece.size,piece.col:piece.col+piece.size]=0

     
        piece.overlay[rowIni:rowFinal,colIni:colFinal]=roi
        piece.overlay[piece.row: piece.row+piece.size,piece.col:piece.col+piece.size]=0
    

        self.pieces.pop((piece.row,piece.col))
        
        piece.changePos(rowIni,colIni)
        

        self.pieces[(rowIni,colIni)]=piece
      
        
        self.opciones.remove(opcion)
        self.limpiarOpciones()
        self.selectedPiece=None
        self.blocked=False
        self.cambiarTurno()


    def borrarPieza(self,piece):
        self.pieces.pop((piece.row,piece.col))
        self.board[piece.row: piece.row+piece.size,piece.col:piece.col+piece.size]=0

        if piece.color =="Red":
            self.red_left-=1
        elif piece.color == "Black":
            self.black_left-=1


    def selection(self, row, col,player):
        print("entro")
        if(player==self.turno):
       
            if len(self.opciones)==0 and not self.blocked:
                self.selectPiece(row,col)
            else :
                bandera=True
                for movimiento in self.opciones :
                    if(movimiento.row<row<(movimiento.row+self.size_square) and  movimiento.col<col<(movimiento.col+self.size_square)):
                        bandera=False
                        self.movePiece(movimiento)
                if bandera and not self.blocked:
                    self.selectPiece(row,col)
        else:
            print("no es su turno")

    def selectPiece(self, row, col):
        pieceS=None

        for key in self.pieces:
            piece= self.pieces[key]

            if(piece.row<row<(piece.row+self.size_square) and  piece.col<col<(piece.col+self.size_square)):
                
                if  piece.color==self.turno:
                    self.limpiarOpciones()
                    self.planificarPieza(piece)
                    self.dibujarOpciones()
                    # self.limpiarOpciones()
                    # self.selectedPiece=(piece.row,piece.col)
                    # self.planificarCampo(piece.row,piece.col,[])
                    # if(piece.king) :
                    #     piece.direction=piece.direction*-1
                    #     self.planificarCampo(piece.row,piece.col,[])
                    #     piece.direction=piece.direction*-1
                
    def planificarPieza(self,piece):
        self.selectedPiece=(piece.row,piece.col)
        self.planificarCampo(piece.row,piece.col,[])
        if(piece.king) :
            piece.direction=piece.direction*-1
            self.planificarCampo(piece.row,piece.col,[])
            piece.direction=piece.direction*-1
        
        

    def limpiarOpciones(self):

        for movimiento in self.opciones:
            self.board[movimiento.row:movimiento.row-self.space+self.size_square,movimiento.col:movimiento.col+self.size_square-self.space]=0
        self.opciones.clear()

    def planificarCampo(self, row,col,listPiezas):
        self.espacioEnBlanco("up",row,col,False,listPiezas)
        self.espacioEnBlanco("down",row,col,False,listPiezas)

        
    def espacioEnBlanco(self,direccion, row,col,enemy,listPiezas):
        
        if direccion=="up":
            newRow= row-self.size_square
            newCol= col+self.size_square*self.pieces[self.selectedPiece].direction

            try:
                newPiece=self.pieces[(newRow,newCol)]
                if newPiece.color!=self.pieces[self.selectedPiece].color:
                    if(not enemy):
                        #listPiezas.append(newPiece)
                        self.espacioEnBlanco(direccion,newRow,newCol,True,listPiezas.copy())
                    
                    
            except KeyError as e:
                if (self.width-(8*self.size_square))<newCol<self.width  and (self.height-(8*self.size_square))<newRow<self.height:
                    if enemy :
                        listPiezas.append(self.pieces[(row,col)])
                        self.planificarCampo(newRow,newCol,listPiezas.copy())
                    self.crearOpcion(row,col,direccion,listPiezas.copy())
               
        
        elif direccion=="down":
            newRow= row+self.size_square
            newCol= col+self.size_square*self.pieces[self.selectedPiece].direction

            try:
                newPiece=self.pieces[(newRow,newCol)]
                if newPiece.color!=self.pieces[self.selectedPiece].color:
                    if(not enemy):
                        #listPiezas.append(newPiece)
                        self.espacioEnBlanco(direccion,newRow,newCol,True,listPiezas.copy()) 
            except KeyError as e:
                if (self.width-(8*self.size_square))<newCol<self.width and (self.height-(8*self.size_square))<newRow<self.height:
                    if enemy :
                        listPiezas.append(self.pieces[(row,col)])
                        self.planificarCampo(newRow,newCol,listPiezas.copy())
                    self.crearOpcion(row,col,direccion,listPiezas.copy())
               

       
    def crearOpcion(self,row,col, direccion ,piezas):
        try: 
            piece=self.pieces[(row,col)]
        except KeyError as e:
            return
        
        if direccion=="up":

            y= int(piece.size/2) + piece.row-self.size_square
                  
            x = int(piece.size/2) + piece.col+self.size_square*self.pieces[self.selectedPiece].direction
                    
            if (self.width-(8*self.size_square))<x<self.width  and (self.height-(8*self.size_square))<y<self.height:

                #cv2.circle(self.board,(x,y),15,(255,0,0),-1)
                newMov= Movimiento(piece.row-self.size_square,piece.col+self.size_square*self.pieces[self.selectedPiece].direction,piezas,self.pieces[self.selectedPiece])
                self.opciones.append(newMov)
            
        
        elif direccion=="down":
                
            y= int(piece.size/2) + piece.row+self.size_square
                  
            x = int(piece.size/2) + piece.col+self.size_square*self.pieces[self.selectedPiece].direction
                    
            if (self.width-(8*self.size_square))<x<self.width and (self.height-(8*self.size_square))<y<self.height:
                #cv2.circle(self.board,(x,y),15,(255,0,0),-1)
                newMov= Movimiento(piece.row+self.size_square,piece.col+self.size_square*self.pieces[self.selectedPiece].direction,piezas,self.pieces[self.selectedPiece])
                self.opciones.append(newMov)
             
    def dibujarOpciones(self):
        piece= self.pieces[self.selectedPiece]
        for opcion in self.opciones:
            y= int(piece.size/2) + opcion.row
                  
            x = int(piece.size/2) + opcion.col

            cv2.circle(self.board,(x,y),15,(255,0,0),-1)
        
        