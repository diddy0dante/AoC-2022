line = open(0).readline()

fourbuf = []

for i, c in enumerate(line):
    fourbuf.append(c)
    if len(fourbuf) > 14:
        fourbuf.pop(0)
        if len(set(fourbuf)) == 14:
            print(i+1)
            break
