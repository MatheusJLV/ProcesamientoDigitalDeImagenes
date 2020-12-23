

class Movimiento:

    def __init__(self, row, col,piezas,pieza):
        self.row = row
        self.col = col
        self.piezas= piezas
        self.pieza=  pieza

    def aumentarPiezas(self,pieza):
        self.piezas.append(pieza)
        