grid = []
for line in open(0):
    grid.append(list(map(int, line.strip())))

width = len(grid[0])
height = len(grid)
count = height * width
scores = []

for i, row in enumerate(grid[1:-1]):
    for j, cell in enumerate(row[1:-1]):
        a, b, c, d = 1, 1, 1, 1

        dx = 1
        while j+1+dx < width-1 and grid[i+1][j+1+dx] < cell:
            dx += 1
            a += 1
        dx = -1
        while j+1+dx > 0 and grid[i+1][j+1+dx] < cell:
            dx -= 1
            b += 1
        dy = 1
        while i+1+dy < height-1 and grid[i+1+dy][j+1] < cell:
            dy += 1
            c += 1
        dy = -1
        while i+1+dy > 0 and grid[i+1+dy][j+1] < cell:
            dy -= 1
            d += 1

        scores.append(a * b * c * d)

print(sorted(scores)[-1])
