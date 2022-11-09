import json
def read_file(path):
    with open(path) as f:
        #  =====================  get level infomation =============
        first_line = f.readline()
        print(first_line)
        row, col, start_x, start_y = [int(x) for x in first_line.split()]
        print(row, " ", col, " ", start_x, " ", start_y)
        print("#  ====================================================")

        #  ================= get level map =============
        game_map = []
        for i in range(row):
            map_line = f.readline().strip()
            list_map_line = map_line.split()
            game_map.append(list_map_line)
        print(game_map)
        print("#  ====================================================")

        #   =============== get level objects ==================
        number_of_object = int(f.readline())
        objects = []
        for i in range(number_of_object):
            lines = ""
            for k in range(7):
                line = f.readline().strip()
                lines += line
            obj = json.loads(lines)
            objects.append(obj)
        print(objects)
        print("#  ====================================================")
        return row, col, start_x, start_y, game_map, objects
