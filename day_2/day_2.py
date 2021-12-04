from typing import Counter
import numpy as np
from pathlib import Path

def load_inputs(input_path):
    """ Load inputs from txt file """
    input_list = np.loadtxt(Path(input_path), dtype=str)
    return input_list

def part_1(input_list):
    """ Solutions for part 1 """
    directions = Counter()
    for command in input_list:
        directions[command[0]] += int(command[1])
    depth = directions['down'] - directions['up']
    answer = depth * directions['forward']

    return answer

def part_2(input_list):
    """ Solutions for part 2 """
    new_directions = Counter()
    for command in input_list:
        new_directions[command[0]] += int(command[1])
        aim = new_directions['down'] - new_directions['up']
        if command[0] == 'forward':
            new_directions['depth'] += int(command[1]) * aim
    answer = new_directions['depth'] * new_directions['forward']

    return answer


def main():
    """ Test solutions and get answers """
    # Test
    test_input_arr = load_inputs('day_2/day_2_test.txt')

    part_1_answer = part_1(test_input_arr)
    assert part_1_answer == 150
    print('Part 1 passed test')

    part_2_answer = part_2(test_input_arr)
    assert part_2_answer == 900
    print('Part 2 passed test')

    # Run
    input_arr = load_inputs('day_2/day_2_inputs.txt')

    part_1_answer = part_1(input_arr)
    print('Part 1: ', part_1_answer)

    part_2_answer = part_2(input_arr)
    print('Part 2: ', part_2_answer)

if __name__ == '__main__':
    main()
