from read_level_input import read_file
level = int(input("choose level (from 1-33)\nYour choice: "))
path = './levels/lvl' + str(level) + '.txt'
row, col, start_x, start_y, bloxorz_map, objects = read_file(path)
print(objects[0]['point'][0][1])