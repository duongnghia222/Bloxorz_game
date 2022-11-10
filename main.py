
from block import Block
from algorithm import BFS
from read_level_input import read_file
import global_variables
from test import test


def main():
    global_variables.init()
    print("\nChoose mode:")
    # is_test = int(input("1. Test all levels\n2. Step by step demo\nYour choice: "))
    global_variables.is_test = 2
    if global_variables.is_test == 1:
        test()
    elif global_variables.is_test == 2:
        screen_scale = 50
        print("Showing step by step...")
        # level = int(input("choose level (from 1-33)\nYour choice: "))
        level = 1
        path = './levels/lvl' + str(level) + '.txt'
        global_variables.row, global_variables.col, global_variables.start_x, \
            global_variables.start_y, game_map, global_variables.objects = read_file(path)
        screen_height = global_variables.row * screen_scale
        screen_width = global_variables.col * screen_scale
        block = Block(global_variables.start_x, global_variables.start_y, "STAND", None, game_map)
        BFS(block)


if __name__ == "__main__":
    main()
