
def sum_neighbors(m, i, j, len_x, len_y):
    pos_x = [0]
    pos_y = [0]

    if i > 0:
        pos_x.append(-1)
    if j > 0:
        pos_y.append(-1)
    if i < len_x:
        pos_x.append(1)
    if j < len_y:
        pos_y.append(1)

    sum_neigh = 0

    for x in pos_x:
        for y in pos_y:
            if x == 0 and y == 0:
                continue
            sum_neigh += m[i + x][j + y]

    return sum_neigh
