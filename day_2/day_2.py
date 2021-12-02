from typing import Counter
import numpy as np
from pathlib import Path

def main(input_path):
    with input_path as f:
        input_list = np.loadtxt(f, dtype=str)

    # Part 1
    directions = Counter()
    for command in input_list:
        directions[command[0]] += int(command[1])
    depth = directions['down'] - directions['up']
    print('Part 1: ', depth * directions['forward'])

    # Part 2
    new_directions = Counter()
    for command in input_list:
        new_directions[command[0]] += int(command[1])
        aim = new_directions['down'] - new_directions['up']
        if command[0] == 'forward':
            new_directions['depth'] += int(command[1]) * aim
    print('Part 2: ', new_directions['depth'] * new_directions['forward'])

if __name__ == '__main__':
    input_path = Path('day_2/day_2_inputs.txt')
    main(input_path)
