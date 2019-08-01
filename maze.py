import random


def maze(height, width):
    # 0 unvisited road
    # 1 unvisited wall
    # 2 visited road
    # 3 visited wall
    # Generate maze map
    map = [[1 for i in range(height)] for i in range(width)]
    for i in range(1, width):
        for j in range(1, height-1):
            if j % 2 != 0 and i % 2 != 0:
                map[i][j] = 0
    # shuffle a start point
    sp = (random.randint(0, width-1), random.randint(0, height-1))
    while map[sp[0]][sp[1]] != 0:
        sp = (random.randint(0, width-1), random.randint(0, height-1))
    point_list = []
    # Start
    map[sp[0]][sp[1]] = 2
    point_list.append((sp[0]-1, sp[1], sp))
    point_list.append((sp[0], sp[1]-1, sp))
    point_list.append((sp[0]+1, sp[1], sp))
    point_list.append((sp[0], sp[1]+1, sp))
    # Loop for generation
    while len(point_list) > 0:
        # shuffle a point in list
        point = point_list[random.randint(0, len(point_list)-1)]
        # check shuffle availability
        if not (0 <= point[0] and point[0] <= width-1 and 0 <= point[1] and point[1] <= height-1):
            point_list.remove(point)
            continue
        # expand
        road = point[2]
        check_point = (point[0]-road[0]+point[0],
                       point[1]-road[1]+point[1])
        if (0 <= check_point[0] and check_point[0] <= width-1 and 0 <= check_point[1] and check_point[1] <= height-1) and map[check_point[0]][check_point[1]] == 0:
            map[check_point[0]][check_point[1]] = 2
            map[point[0]][point[1]] = 2
            # add around points of check_point
            if check_point[0] >= 0 and map[check_point[0]-1][check_point[1]] == 1:
                point_list.append(
                    (check_point[0]-1, check_point[1], check_point))
            if check_point[0] <= width-1 and map[check_point[0]+1][check_point[1]] == 1:
                point_list.append(
                    (check_point[0]+1, check_point[1], check_point))
            if check_point[1] >= 0 and map[check_point[0]][check_point[1]-1] == 1:
                point_list.append(
                    (check_point[0], check_point[1]-1, check_point))
            if check_point[1] <= height-1 and map[check_point[0]][check_point[1]+1] == 1:
                point_list.append(
                    (check_point[0], check_point[1]+1, check_point))
        # remove from list
        point_list.remove(point)

    # output
    for x in map:
        for y in x:
            if y == 0 or y == 2:
                print(' ', end='')
            else:
                print('▉', end='')
        print()
    print()


maze(111, 111)
