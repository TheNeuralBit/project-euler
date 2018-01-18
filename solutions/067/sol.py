import sys

with open('triangle.txt', 'r') as fp:
    triangle = [list(map(int, line.strip().split(' '))) for line in fp]

# iterate from the bottom up. From each node, decide if it would be better to
# go left or right, then sum that value
# repeat all the way up...
for r in range(len(triangle) - 2, -1, -1):
    row = triangle[r]
    below = triangle[r+1]
    for x in range(len(row)):
        row[x] += max(below[x], below[x+1])

# ... then the answer is at the top
print(triangle[0][0])
