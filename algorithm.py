import global_variables
from functions import check_win, add_move, view_2D_solution


def BFS(block):
    global_variables.previous = [block]  # save previous states
    queue = [block]
    while queue:
        current = queue.pop(0)
        if check_win(current):
            view_2D_solution(current)
            print("Success!\nCalculated steps:", 99999999)
            return True

        if current.status != "SPLIT":  # if this is a complete block then it can move 4 directions
            add_move(queue, current.move_up())
            add_move(queue, current.move_right())
            add_move(queue, current.move_down())
            add_move(queue, current.move_left())

        else:
            add_move(queue, current.split_move_up())
            add_move(queue, current.split_move_right())
            add_move(queue, current.split_move_down())
            add_move(queue, current.split_move_left())

            add_move(queue, current.split_move_up_other())
            add_move(queue, current.split_move_right_other())
            add_move(queue, current.split_move_down_other())
            add_move(queue, current.split_move_left_other())
    print("Can not find the answer  :((")
    return False


