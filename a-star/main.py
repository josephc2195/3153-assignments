import numpy as np
from numpy import random as ra

class Star:
        def __init__(self):

                self.board = np.empty((15, 15), dtype=object)

                for i in range(15):
                        for x in range(15):
                                ten = ra.randint(1, 10)
                                if ten != 1:
                                        self.board[i][x] = 0
                                else:
                                        self.board[i][x] = 1
                print("Here is your starting board:")
                self.showBoard(self.board)
                self.startRow, self.startCol = self.getStart()
                self.goalRow, self.goalCol = self.getGoal()
                self.openList = [(self.startRow, self.startCol)]
                self.board[self.startRow][self.startCol] = 'S'
                self.board[self.goalRow][self.goalCol] = 'G'
                cont = self.confirmBoard(self.board)
        
        def showBoard(self, board):
                print(board)

                
        def getStart(self):
                row = int(input('Now, enter the row you want the starting node to be on (1-15): ')) - 1 
                col = int(input('Enter the column you want the starting node to be on (1-15): ')) - 1 
                startCoords = (row, col)
                return startCoords

        def getGoal(self):
                row = int(input('Enter the row you want the goal node to be on (1-15): ')) - 1
                col = int(input('Enter the column you want the goal node to be on (1-15): ')) -1
                goalCoords = (row, col)
                return goalCoords

        def confirmBoard(self, board):
                print('This is your current board: ')
                print(board)
                cont = input('Would you like to continue? ')
                if cont.lower() == 'yes' or cont.lower() == 'y':
                        return True
                else:
                        return 0
        def getH(self, goalRow, goalCol, startRow, startCol):
                currentH = 0
                if goalCol > startCol:
                        currentH += goalCol - startCol
                else:
                        currentH += startCol - goalCol
                if goalRow > startRow:
                        currentH += goalRow - startRow
                else:
                        currentH += startRow - goalRow
                print(f'Current H: {currentH}')

Star()
                