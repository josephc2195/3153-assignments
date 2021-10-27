class Node:
        def __init__(self, r, c, t):
                self.row = r
                self.col = c
                self.type = t

        def setF(self):
                self.f = g+h
        
        def setG(self, value):
                self.g = value
        
        def setH(self, value):
                self.h = value
        
        def setParent(self, n):
                self.parent = n 
        
        def getF(self):
                return self.f
        def getH(self):
                return self.h
        def getG(self):
                return self.g
        def getParent(self):
                return self.parent
        def getRow(self):
                return self.row 
        def getCol(self):
                return self.col
        def equals(self, obj):
                self.n = obj
                return self.row == self.n.getRow() and self.col == self.n.getCol()
                

