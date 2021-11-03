import timeit

N = int(input('Enter N : '))
print('')
numSol = 0
b = N * [-1]
colFree = N * [1]
upFree = (2 * N - 1) * [1]
downFree = (2 * N - 1) * [1]
start = timeit.default_timer()


def printBoard(b):
    print(b)


def putQueen(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N):
        if colFree[c] and upFree[r + c] and downFree[r - c + N - 1]:
            b[r] = c
            colFree[c] = upFree[r + c] = downFree[r - c + N - 1] = 0
            if r == N - 1:
                printBoard(b)
                numSol += 1
            else:
                putQueen(r + 1, b, colFree, upFree, downFree)
            colFree[c] = upFree[r + c] = downFree[r - c + N - 1] = 1


putQueen(0, b, colFree, upFree, downFree)
print()
print('Input: ', N)
print('number of solutions = ', numSol)
print('--------------------------------------')
end = timeit.default_timer()
print('Time : ' + str(end - start) + ' s')