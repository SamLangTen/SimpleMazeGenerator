import random


def maze(height, width):
    # Generate maze map
    map = [[1 for i in range(height)] for i in range(width)]
    # shuffle a start point
    sp = (random.randint(0, width-1), random.randint(0, height-1))
    point_list = []
    # Start
    map[sp[0]][sp[1]] = 0
    point_list.append((sp[0]-1, sp[1]))
    point_list.append((sp[0], sp[1]-1))
    point_list.append((sp[0]+1, sp[1]))
    point_list.append((sp[0], sp[1]+1))
    # Loop for generation
    while len(point_list) > 0:
        # shuffle a point in list
        point = point_list[random.randint(0, len(point_list)-1)]
        # check shuffle availability
        if not (0 <= point[0] and point[0] <= width-1 and 0 <= point[1] and point[1] <= height-1):
            point_list.remove(point)
            continue
        # check around points
        roads = []
        if point[0] != 0 and map[point[0]-1][point[1]] == 0 and point[0]+1 != width:
            roads.append((point[0]-1, point[1]))
        if point[1] != 0 and map[point[0]][point[1]-1] == 0 and point[1]+1 != height:
            roads.append((point[0], point[1]-1))
        if point[0] != width - 1 and map[point[0]+1][point[1]] == 0 and point[0]-1 >= 0:
            roads.append((point[0]+1, point[1]))
        if point[1] != height - 1 and map[point[0]][point[1]+1] == 0 and point[1]-1 >= 0:
            roads.append((point[0], point[1]+1))
        if len(roads) > 0:
            road = roads[random.randint(0, len(roads)-1)]
            check_point = (point[0]-road[0]+point[0], point[1]-road[1]+point[1])
            # if checkpoint is wall
            if map[check_point[0]][check_point[1]] == 1:
                # let checkpoint and point as road
                map[check_point[0]][check_point[1]] = 0
                map[point[0]][point[1]] = 0
                # add check_point's around points
                point_list.append((check_point[0]-1, check_point[1]))
                point_list.append((check_point[0], check_point[1]-1))
                point_list.append((check_point[0]+1, check_point[1]))
                point_list.append((check_point[0], check_point[1]+1))
        # remove from list
        point_list.remove(point)

    # output
    for x in map:
        for y in x:
            if y == 0:
                print(' ', end='')
            else:
                print('▉', end='')
        print()
    print()


maze(10, 10)
