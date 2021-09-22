import numpy as np

board = [[0 for i in range(8)] for x in range(8)]
qPlacement = []
npq = np.array(qPlacement)
h = 0
for i in board:
        y = np.random.randint(0, 8)
        i[y] = 1
        npq = np.append(npq, y)
        print(i)
if len(npq) != len(set(npq)):
        h += len(npq) - len(set(npq))

for x in range(8):
        for y in range(8):
                if y < 7: 
                        if board[x][y+1]:
                                h+=1
                elif y > 0:
                        if board[x][y-1]:
                                h+=1
print(h)

