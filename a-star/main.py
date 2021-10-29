import numpy as np
from numpy import random as ra
from Node import Node
import pygame
import sys
from queue import PriorityQueue

class Star:
        def __init__(self):
                cont = False
                while cont == False:
                        self.board = np.empty((15, 15), dtype=Node)
                        self.openList = np.empty((15, 15), dtype=Node)
                        self.closedList = np.empty((15, 15), dtype=Node)

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
                        self.openList[0] = [(self.startRow, self.startCol)]
                        self.board[self.startRow][self.startCol] = 'S'
                        self.board[self.goalRow][self.goalCol] = 'G'
                        cont = self.confirmBoard(self.board)
                        self.actions()
                        
                self.currentH = self.calcH(self.goalRow, self.goalCol, self.startRow, self.startCol)
        
        def setF(self):
                self.f = self.g+self.h
        
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
        
        def showBoard(self, board):
                for i, x in enumerate(board):
                        if(i<9):
                                print(str(i+1)+ ' ' + str(x))
                        else: 
                                print(str(i+1) + '' + str(x))

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
                        return False

        def calcH(self, goalRow, goalCol, startRow, startCol):
                currentH = 0
                if goalCol > startCol:
                        currentH += goalCol - startCol
                else:
                        currentH += startCol - goalCol
                if goalRow > startRow:
                        currentH += goalRow - startRow
                else:
                        currentH += startRow - goalRow
                currentH *= 10
                print(f'Current H: {currentH}')
        
        def actions(self):
                while len(self.openList) != 0:
                        currentNode = self.findLowestF()
                        self.openList = np.delete(self.openList, currentNode)
                        print(currentNode)

                        #if self.currentNode == goalNode:

        #def findNbrs(self, currentNode):


                        
        
        


        

Star()
                