import numpy as np
from pathlib import Path

def load_inputs(boards_path, calls_path):
    """ Load inputs from txt files """
    input_path = Path(boards_path)
    boards_arr = np.loadtxt(input_path, dtype=int)

    input_path = Path(calls_path)
    calls_arr = np.loadtxt(input_path, dtype=int, delimiter=',')

    return boards_arr, calls_arr

def part_1(boards_arr, calls_arr):
    """ Answer for part 1 """
    N = int(boards_arr.shape[0] / 5)
    boards_list = np.split(boards_arr, N)
    mask = np.ones(boards_arr.shape, dtype=bool)
    for call in calls_arr:
        call_mask = np.where(boards_arr == call)
        mask[call_mask] = False
        mask_list = np.split(mask, N)
        for i, board_mask in enumerate(mask_list):
            row_sum = np.sum(board_mask, axis=1)
            col_sum = np.sum(board_mask, axis=0)
            if np.any(row_sum == 0) or np.any(col_sum == 0):
                break
        else:
            continue
        break

    winning_board = boards_list[i]
    unmarked = winning_board[board_mask]
    unmarked_sum = np.sum(unmarked)
    answer = unmarked_sum * call

    return answer

def part_2(boards_arr, calls_arr):
    """ Answer for part 2 """
    N = int(boards_arr.shape[0] / 5)
    boards_list = np.split(boards_arr, N)
    all_boards = list(range(N))
    mask = np.ones(boards_arr.shape, dtype=bool)
    for call in calls_arr:
        call_mask = np.where(boards_arr == call)
        mask[call_mask] = False
        mask_list = np.split(mask, N)
        for i in all_boards:
            board_mask = mask_list[i]
            row_sum = np.sum(board_mask, axis=1)
            col_sum = np.sum(board_mask, axis=0)
            if np.any(row_sum == 0) or np.any(col_sum == 0):
                all_boards.remove(i)
            if len(all_boards) == 0:
                break
        else:
            continue
        break

    losing_board = boards_list[i]
    unmarked = losing_board[board_mask]
    unmarked_sum = np.sum(unmarked)
    answer = unmarked_sum * call

    return answer

def main():
    """ Test solutions and get answers """
    # Test
    test_boards_path = 'day_4/day_4_test_boards.txt'
    test_calls_path = 'day_4/day_4_test_calls.txt'
    test_boards_arr, test_calls_arr = load_inputs(test_boards_path, test_calls_path)

    part_1_answer = part_1(test_boards_arr, test_calls_arr)
    assert part_1_answer == 4512
    print('Part 1 passed test')

    part_2_answer = part_2(test_boards_arr, test_calls_arr)
    assert part_2_answer == 1924
    print('Part 2 passed test')

    # Run
    boards_path = 'day_4/day_4_inputs_boards.txt'
    calls_path = 'day_4/day_4_inputs_calls.txt'
    boards_arr, calls_arr = load_inputs(boards_path, calls_path)

    part_1_answer = part_1(boards_arr, calls_arr)
    print('Part 1: ', part_1_answer)

    part_2_answer = part_2(boards_arr, calls_arr)
    print('Part 2: ', part_2_answer)

if __name__ == '__main__':
    main()
