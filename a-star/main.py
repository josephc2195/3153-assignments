import numpy as np
from numpy import random as ra

class Star:
        def __init__(self):

                board = np.empty((15, 15), dtype=object)

                for i in range(15):
                        for x in range(15):
                                ten = ra.randint(1, 10)
                                if ten != 1:
                                        board[i][x] = 0
                                else:
                                        board[i][x] = 1
                self.startRow, self.startCol = self.getStart()
                self.goalRow, self.goalCol = self.getGoal()
                self.openList = [(self.startRow, self.startCol)]
                self.board[self.startRow][self.startCol] = 'S'
                self.board[self.goalRow][self.goalCol] = 'G'

                
                
                

                
        def getStart(self):
                row = int(input('Enter the row you want the starting node to be on: '))
                col = int(input('Enter the column you want the starting node to be on: '))
                startCoords = (row, col)
                return startCoords

        def getGoal(self):
                row = input('Enter the row you want the goal node to be on: ')
                col = input('Enter the column you want the goal node to be on: ')
                goalCoords = (row, col)
                return goalCoords

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

                