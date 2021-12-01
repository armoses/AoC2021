import numpy as np
from pathlib import Path

def main(input_path):
    with input_path as f:
        input_list = np.loadtxt(f)

    # Part 1
    count = 0
    for i in range(len(input_list) - 1):
        if input_list[i + 1] > input_list[i]:
            count += 1
    print('Part 1: ', count)

    # Part 2
    count = 0
    for i in range(len(input_list) - 3):
        this_sum = input_list[i] + input_list[i+1] + input_list[i+2]
        next_sum = input_list[i+1] + input_list[i+2] + input_list[i+3]
        if next_sum > this_sum:
            count += 1
    print('Part 2: ', count)

if __name__ == '__main__':
    input_path = Path('day_1/day_1_inputs.txt')
    main(input_path)
