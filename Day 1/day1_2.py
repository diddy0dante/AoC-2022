import fileinput

elves = [[]]

for line in fileinput.input():
    line = line.strip()
    if line == '':
        elves.append([])
    else:
        elves[-1].append(int(line))

print(sum(sorted(list(map(sum, elves)))[-3:]))
