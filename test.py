import global_variables
from read_level_input import read_file
from block import Block
from algorithm import BFS
import time


def test():
    for level in range(1,10):
        path = './levels/lvl' + str(level) + '.txt'
        global_variables.init()
        global_variables.row, global_variables.col, global_variables.start_x, \
            global_variables.start_y, game_map, global_variables.objects = read_file(path)
        block = Block(global_variables.start_x, global_variables.start_y, "STAND", None, game_map)
        start_time = time.time()
        print("Testing level", level, " ..........")
        success = BFS(block)
        if success:
            print("Success !!!")
            print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 5), ("s"))
        else:
            print("Failed to find solution :( ")
        print("===========================================")