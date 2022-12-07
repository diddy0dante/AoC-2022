line = open(0).readline()

fourbuf = []

for i, c in enumerate(line):
    fourbuf.append(c)
    if len(fourbuf) > 4:
        fourbuf.pop(0)
        if len(set(fourbuf)) == 4:
            print(i+1)
            break
