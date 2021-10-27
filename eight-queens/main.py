from numpy import random
class Queens:

        #initializes the class and variables needed for class:
        def __init__(self):
                self.restarts = 0
                self.moves = 0
                self.board = self.makeBoard()

                #gets the current number of heuristic 
                self.h = self.countH(self.board)
                print(f'Current H: {self.h}')
                print('Current State:')
                self.showBoard(self.board)

                self.actions(self.board, self.moves, self.restarts)

        #creates empty 2d array 
        def makeEmptyBoard(self):
                return [[0 for i in range(8)] for x in range(8)]

        #creates empty 2d array
        def makeBoard(self):
                board = [[0 for i in range(8)] for x in range(8)]

                #adds a random 1(represents a queen) to each column
                for i in range(8):
                        board[random.randint(0, 8)][i] = 1                
                return board

        def showBoard(self, board):
                for i in board:
                        print(i)

        def actions(self, board, moves, r):
                copy_of_board =[]

                #this is where all heuristic values are stored for every possible move
                hValues = self.makeEmptyBoard()
                n = 7
                h = self.countH(board)

                print(f'Neighbors found with lower H: {n}')
                print('Setting new current state...')
                print('')

                while(h != 0):
                        copy_of_board = [row.copy() for row in board]
                        
                        for c in range(8):
                                for i in range(8):
                                        #making the column with a queen all 0's
                                        copy_of_board[i][c] = 0

                                for i in range(8):
                                        #note the queen position in the original board
                                        if board[i][c] == 1:
                                                qRow = i
                                        
                                        #adds a 1 to the start of the column and 
                                        #calculates the H value for if the queen moves there
                                        copy_of_board[i][c] = 1
                                        hValues[i][c] = self.countH(copy_of_board)
                                        copy_of_board[i][c] = 0
                                copy_of_board[qRow][c] = 1
                        
                        #checks if there are no neighbors with lower h value.
                        if self.startOver(hValues, n):
                                print("Restarting...")
                                r += 1
                                board = self.makeBoard()
                        
                        #assigns the smallest h value to move the queen to said value
                        row, col, n = self.getSmallestH(hValues, n, h)
                       
                        #changing all values in queens column to 0
                        for i in range(8):
                                board[i][col] = 0
                        
                        #moves the queen to the smallest h value.
                        board[row][col] = 1
                        moves += 1
                        h = self.countH(board)
                        
                        #
                        if self.countH(board) == 0:
                                print(f'Current H: {h}')
                                print('Current State:')
                                self.showBoard(board)
                                print('Solution Found!')

                                print(f'State changes: {moves}')
                                print(f'Restarts: {r}')

                        else:
                                print(f'Current H: {h}')
                                print('Current State:')
                                self.showBoard(board)
                                print(f'Neighbors found with lower H: {n}')
                                print('Setting new current state...')
                                print('')

        def countH(self, board):
                collisions = 0
                #iterates through the board to see how many collisions queens have
                for i in range(8):
                        for x in range(8):
                                if board[i][x]:
                                        col = self.colCheck(board, i)
                                        row = self.rowCheck(board, x)
                                        diag = self.diagnalCheck(board, i, x)
                                        if(col or diag or row):
                                                collisions += 1
                return collisions

        def colCheck(self, board, x):
                c = 0
                for i in range(8):
                        if board[x][i]:
                                c += 1
                if c > 1:
                        return True

        def rowCheck(self, board, x):
                c = 0
                for i in range(8):
                        if board[i][x] == 1:
                                c +=1
                if c > 1:
                        return True

        def diagnalCheck(self, board, x, n):
                for i in range(1, 8):
                        if x+i < 7 and n+i < 7:
                                if board[x+i][n+i]:
                                        return True
                        if x-i >= 0 and n-i >=0:
                                if board[x-i][n-i]:
                                        return True
                        if x+i < 7 and n-i >=0:
                                if board[x+i][n-i]:
                                        return True
                        if x-i >= 0 and n+i < 7:
                                if board[x-i][n+i]:
                                        return True


        def startOver(self, hArr, n):
                minH = 8 
                for i in range(8):
                        for x in range(8):
                                if hArr[i][x] < minH:
                                        minH = hArr[i][x]
                
                if n == 0:
                        return True
        
        def getSmallestH(self, hArr, n, h):
                minH = 8
                count = 0
                #iterates through heuristic values to find lowest. 
                #returns column and row value of the smallest value. 
                for i in range(8):
                        for x in range(8):
                                if hArr[i][x] < minH:
                                        minH = hArr[i][x]
                                        col = x
                                        row = i
                                #if there is a lower neighbor it adds to the count
                                if hArr[i][x] < h:
                                        count += 1
                #count gets assigned to neighbor.
                n = count
                cord = (row, col, n)
                return cord

Queens()
