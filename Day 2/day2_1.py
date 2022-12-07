import fileinput

score = 0

for line in fileinput.input():
    opp_s, me_s = line.strip().split(' ')
    opp = (ord(opp_s) - 65) % 3 + 1
    me = (ord(me_s) - 88) % 3 + 1
    score += me
    if me == opp:
        score += 3
    elif (me-1 == (opp)%3):
        score += 6

print(score)
