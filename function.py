import numpy as np
import copy

def get_state(level):
    map_level = open(level, 'r')  # for read only
    row, col, start_x, start_y = [int(x) for x in next(map_level).split()]
    map_level.close()
    return row, col, start_x, start_y


def get_objects(level, row):
    map_level = open(level, 'r')
    line_count = 1
    objects = []
    for line in map_level:
        line_count += 1
        if line_count > row+2:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            objects.append(line_list)
    elements = np.array(copy.deepcopy(objects), dtype=object)
    int_obj = []
    if len(elements) == 0:
        print('no object')
        return objects
    else:
        for i in elements:
            for j in elements:
                int_obj = [[int(i) for i in j] for j in elements]
    print(np.matrix(int_obj))
    map_level.close()
    return int_obj

def get_map(level, row):
    map_level = open(level, 'r')
    map_view = []
    content = map_level.readlines()
    for line in content[1:row + 1]:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        map_view.append(line_list)
    map_level.close()
    return map_view
