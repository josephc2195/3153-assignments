import numpy as np

class Queens:

        def __init__(self):
                self.restarts = 0
                self.moves = 0
                self.board = self.makeBoard()
                h = 0
                print(f'Current H: {h}')
                print('Current State:')
                self.showBoard(self.board)
                self.actions(self.board, self.moves, self.restarts)

        def makeEmptyBoard(self):
                return [[0 for i in range(8)] for x in range(8)]

        def makeBoard(self):
                board = [[0 for i in range(8)] for x in range(8)]
                for i in range(8):
                        board[np.random.randint(0, 8)][i] = 1                
                return board

        def showBoard(self, board):
                for i in board:
                        print(i)

        def rowCheck(self, board, x):
                c = 0
                for i in range(8):
                        if board[i][x] == 1:
                                c +=1
                if c > 1:
                        return True


        def colCheck(self, board, x):
                c = 0
                for i in range(8):
                        if board[i][x]:
                                c += 1
                if c > 1:
                        return True

        def diagnalCheck(self, board, x, n):
                c = 0
                for i in range(1, 8):
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
                for i in range(8):
                        for x in range(8):
                                if board[i][x]:
                                        col = self.colCheck(board, i)
                                        row = self.rowCheck(board, x)
                                        diag = self.diagnalCheck(board, i, x)
                                        if(col or diag or row):
                                                collisions += 1
                return collisions

        def actions(self, board, moves, r):
                copyBoard =[]
                hArray = self.makeEmptyBoard()
                prevSpot = 0
                solved = False
                n = 8
                h = 0 

                while(solved == False):
                        colCount = 0

                        for i in range(8):
                                copyBoard.append(board[i])
                                
                        while colCount < 8:
                                for i in range(8):
                                        copyBoard[i][colCount] = 0
                                for i in range(8):
                                        if board[i][colCount] == 1:
                                                prevSpot = i
                                        copyBoard[i][colCount] = 1
                                        hArray[i][colCount] = self.countH(copyBoard)
                                        copyBoard[i][colCount] = 0
                                copyBoard[prevSpot][colCount] = 1
                                colCount += 1
                        if self.determineRestart(hArray, n):
                                print("Restarting...")
                                r += 1
                                board = self.makeBoard()
                        minCol = self.findMinCol(hArray, n, h)
                        minRow = self.findMinRow(hArray, n, h)
                        for i in range(8):
                                board[i][minCol] = 0
                        board[minRow][minCol] = 1
                        moves += 1
                        h = self.countH(board)

                        if self.countH(board) == 0:
                                print('Current State:')
                                self.showBoard(board)
                                print('Solution Found!')

                                print(f'State changes: {moves}')
                                print(f'Restarts: {r}')
                                solved = True
                        else:
                                print(f'Current H: {h}')
                                print('Current State:')
                                self.showBoard(board)
                                print(f'Neighbors found with lower h: {n}')
                                print('Setting new current state')
                                print('')

                        
                

        def findMinCol(self, hArr, n, h):
                minCol = 0
                minVal = 0
                count = 0

                for i in range(8):
                        for x in range(8):
                                if hArr[i][x]:
                                        minVal = hArr[i][x]
                                        minCol = x
                                if hArr[i][x] < h:
                                        count += 1
                n = count
                return minCol
        
        def findMinRow(self, hArr, n, h):
                minRow = 8
                minVal = 8

                for i in range(8):
                        for x in range(8):
                                if hArr[i][x]:
                                        minVal = hArr[i][x]
                                        minRow = i  
                return minRow
                


        def determineRestart(self, hArr, n):
                minH = 8 
                for i in range(8):
                        for x in range(8):
                                if hArr[i][x] < minH:
                                        minH = hArr[i][x]
                
                if n == 0:
                        return True
q = Queens()
