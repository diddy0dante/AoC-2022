import fileinput

dirs = {}

input = fileinput.input()

def recursive_search(name):
    dir_size = 0
    try:
        while True:
            line = next(input).strip().split(' ')
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '/':
                        pass
                    elif line[2] == '..':
                        dirs[name] = dir_size
                        return dirs[name]
                    else:
                        dir_size += recursive_search(name+line[2]+'/')
            elif line[0].isnumeric():
                dir_size += int(line[0])
    except StopIteration:
        dirs[name] = dir_size
        return dirs[name]

dirs['/'] = recursive_search('/')

required_space = dirs['/'] - 40000000
dir_list = [dirs[key] for key in dirs]
result = sorted(filter((lambda x: x >= required_space), dir_list))[0]
print(result)
