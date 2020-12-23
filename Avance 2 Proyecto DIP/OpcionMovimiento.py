

class Movimiento:

    def __init__(self, row, col,piezas):
        self.row = row
        self.col = col
        self.piezas= piezas
       

    def aumentarPiezas(self,pieza):
        self.piezas.append(pieza)
        