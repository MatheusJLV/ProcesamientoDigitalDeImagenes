


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



