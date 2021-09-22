import numpy as np

def calculateH(queens):
        h=0
        if len(queens) != len(set(queens)):
                h += len(queens) - len(set(queens))

        for x in range(8):
                for y in range(8):
                        if y < 7: 
                                if board[x][y+1]:
                                        h+=1
                        elif y > 0:
                                if board[x][y-1]:
                                        h+=1
        return h

def makeBoard():
        return [[0 for i in range(8)] for x in range(8)]

h = 0
board = makeBoard()
qPlacement = []
npq = np.array(qPlacement)

for i in board:
        y = np.random.randint(0, 8)
        i[y] = 1
        npq = np.append(npq, y)
        print(i)
currentH = calculateH(npq)
print(currentH)
lowest = npq
lowH = h

for i in range(8):
        if(i > 0):
                npq[i] = npq[i]-1
                if(currentH > calculateH(npq)):
                        lowH = calculateH(npq)
                        lowest = npq
                        

        elif(i < 7):
                npq[i] = npq[i]+1
                if(currentH > calculateH(npq)):
                        lowH = calculateH(npq)
                        lowest = npq



                
