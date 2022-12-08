grid = []
for line in open(0):
    grid.append(list(map(int, line.strip())))

grid_t = list(zip(*grid))
count = len(grid) * len(grid[0])

for i, row in enumerate(grid[1:-1]):
    for j, cell in enumerate(row[1:-1]):
        a = [t >= cell for t in grid[i+1][:j+1]]
        b = [t >= cell for t in grid[i+1][j+2:]]
        c = [t >= cell for t in grid_t[j+1][:i+1]]
        d = [t >= cell for t in grid_t[j+1][i+2:]]
        if all([any(a), any(b), any(c), any(d)]):
            count -= 1

print(count)
