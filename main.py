
from block import Block
from algorithm import BFS
from read_level_input import read_file
import global_variables
import functions
import algorithm


def main():
    print("\nChoose mode:")
    # is_test = int(input("1. Test all levels\n2. Step by step demo\nYour choice: "))
    is_test = 2
    if is_test == 1:
        print("testing...")
    elif is_test == 2:
        screen_scale = 50
        print("Showing step by step...")
        # level = int(input("choose level (from 1-33)\nYour choice: "))
        level = 1
        path = './levels/lvl' + str(level) + '.txt'
        global_variables.init()
        row, col, start_x, start_y, game_map, objects = read_file(path)
        screen_height = row * screen_scale
        screen_width = row * screen_scale
        block = Block(start_x, start_y, "STAND", None, game_map)
        BFS(block)


if __name__ == "__main__":
    main()
