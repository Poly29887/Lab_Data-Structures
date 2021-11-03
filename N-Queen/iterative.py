import timeit
from itertools import permutations

N = int(input('Enter N : '))
print('')
start = timeit.default_timer()


def print_table():
    for row in range(N):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(N):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= N-1 and x+m <= N-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= N-1:
                table[y-m][x+m] = 1
            if y+m <= N-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

table = [[0]*N for _ in range(N)]
perms = permutations([i for i in range(N)])
num_comb = 0
round = 0
for perm in perms:
    for i in range(N):
        if put_queen(perm[i], i) == True:
            round += 1
        else:
            round = 0
            break
    if round  == N:
        round = 0
        print_table()
        num_comb += 1
        print(f"solution{num_comb}")
        print(" ")

    table = [[0] * N for _ in range(N)]
print('Input: ',N)
print('Number of solution: ', num_comb)
print('--------------------------------------')
end = timeit.default_timer()
print('Time : ' + str(end - start) + ' s')