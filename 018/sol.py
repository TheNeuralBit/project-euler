import sys

with open('triangle.txt', 'r') as fp:
    triangle = [list(map(int, line.strip().split(' '))) for line in fp]

for r in range(len(triangle) - 2, -1, -1):
    row = triangle[r]
    below = triangle[r+1]
    for x in range(len(row)):
        row[x] += max(below[x], below[x+1])

print(triangle[0][0])
