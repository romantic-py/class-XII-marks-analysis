from mainfile import master

master.sort(key=lambda x: x[0], reverse=True)
prev = master[0][0]

rank = 1
with open('rank_list.txt', 'w') as out:
    for m in master:
        if m[0] < prev:
            prev = m[0]
            rank += 1
        out.write('{} {} {}\n'.format(str(rank).zfill(3), m[0], m[1]))