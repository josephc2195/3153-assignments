import numpy as np

class Queens:
        def __init__(self):
                self.board = self.makeBoard()
                h = self.countH(self.board)
                print(f'Current H: {h}')
                self.showBoard(self.board)

        def makeBoard(self):
                board = [[0 for i in range(8)] for x in range(8)]
                for i in board:
                        i[np.random.randint(0, 8)] = 1                
                return board

        def showBoard(self, board):
                for i in board:
                        print(i)

        def vertCollisions(self, board, x):
                c = 0
                for i in range(8):
                        if board[i][x]:
                                c += 1
                if c > 0:
                        return True

        def diagnalCollisions(self, board, x, n):
                c = 0
                for i in range(8):
                        if x+i < 7 and n+i < 7:
                                if board[x+i][n+i]:
                                        c += 1
                        if x-i >= 0 and n-i >=0:
                                if board[x-i][n-i]:
                                        c += 1
                        if x+i < 7 and n-i >=0:
                                if board[x+i][n-i]:
                                        c += 1
                        if x-i >= 0 and n+i < 7:
                                if board[x-i][n+i]:
                                        c += 1
                if c > 1:
                        return True

        def countH(self, board):
                collisions = 0
                verts = False
                diag = False

                for i in range(8):
                        for x in range(8):
                                if board[i][x]:
                                        verts = self.vertCollisions(board, x)
                                        diag = self.diagnalCollisions(board, i, x)
                                        if(verts or diag):
                                                collisions += 1
                return collisions

        

q = Queens()
