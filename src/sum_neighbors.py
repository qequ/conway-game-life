
def sum_neighbors(m, i, j, len_x, len_y):
    pos_x = [-1, 0, 1]
    pos_y = [-1, 0, 1]

    sum_neigh = 0

    for x in pos_x:
        for y in pos_y:
            if (x == 0 and y == 0) or (i + x < 0) or (j + y < 0) or (i + x > len_x) or (j + y > len_y):
                continue
            sum_neigh += m[i + x][j + y]

    return sum_neigh
