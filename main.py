import numpy as np

def makeBoard():
        return [[0 for i in range(8)] for x in range(8)]

def addRandQueens(board):
        for i in board:
                y = np.random.randint(0, 8)
                i[np.random.randint(0,8)] = 1
                npq = np.append(npq, y)

def vertCollisions(board, x):
        collisions = 0
        for i in range(8):
                if board[i][x]:
                        collisions += 1
        if collisions > 0:
                return True
def diagnalCollisions(board, x, n):
        collisions = 0
        for i in range(8):
                if x+i < 7 and n+i < 7:
                        if board[x+i][n+i]:
                                collisions += 1
                if x-1 >= 0 and n-i >=0:
                        if board[x-i][n-i]:
                                collisions += 1
                if x+1 < 7 and n-i >=0:
                        if board[x+i][n-i]:
                                collisions += 1
                if x-1 >= 0 and n+i < 7:
                        if board[x-i][n+i]:
                                collisions += 1
        if collisions > 1:
                return True

def countH(board):
        collisions = 0
        verts = False
        diag = False

        for i in range(8):
                for x in range(8):
                        if board[i][x]:
                                verts = vertCollisions(board, x)
                                diag = diagnalCollisions(board, i, x)
                                if(vers or diag):
                                        collisions += 1
        return collisions



