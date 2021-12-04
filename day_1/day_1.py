import numpy as np
from pathlib import Path

def load_inputs(input_path):
    """ Load inputs from txt file """
    input_list = np.loadtxt(Path(input_path))
    return input_list

def part_1(input_list):
    """ Solution for part 1 """
    count = 0
    for i in range(len(input_list) - 1):
        if input_list[i + 1] > input_list[i]:
            count += 1

    return count

def part_2(input_list):
    """ Solution for part 2 """
    count = 0
    for i in range(len(input_list) - 3):
        this_sum = input_list[i] + input_list[i+1] + input_list[i+2]
        next_sum = input_list[i+1] + input_list[i+2] + input_list[i+3]
        if next_sum > this_sum:
            count += 1

    return count

def main():
    """ Test solutions and get answers """
    # Test
    test_input_arr = load_inputs('day_1/day_1_test.txt')

    part_1_answer = part_1(test_input_arr)
    assert part_1_answer == 7
    print('Part 1 passed test')

    part_2_answer = part_2(test_input_arr)
    assert part_2_answer == 5
    print('Part 2 passed test')

    # Run
    input_arr = load_inputs('day_1/day_1_inputs.txt')

    part_1_answer = part_1(input_arr)
    print('Part 1: ', part_1_answer)

    part_2_answer = part_2(input_arr)
    print('Part 2: ', part_2_answer)

if __name__ == '__main__':
    main()
