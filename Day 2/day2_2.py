import fileinput

score = 0

for line in fileinput.input():
    opp_s, me_s = line.strip().split(' ')
    opp = (ord(opp_s) - 65) % 3
    me = (ord(me_s) - 88) % 3
    score += me * 3
    score += (opp + (me-1)) % 3 + 1

print(score)
