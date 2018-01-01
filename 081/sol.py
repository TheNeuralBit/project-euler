def traverse(matrix):
    pos = (len(matrix) - 1, len(matrix[0]) - 1)
    for y, row in reversed(enumerate(matrix)):
        for x in range(len(row) - 1, -1, -1):
            matrix[y][x] =
    matrix[pos[0]][pos[1]]

with open('matrix.txt', 'r') as fp:
    matrix = [list(map(int, line.strip().split(','))) for line in fp]
