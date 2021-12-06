import numpy as np
from pathlib import Path
import pandas as pd


def load_inputs(input_path):
    """ Load inputs from txt file """
    input_list = np.loadtxt(Path(input_path), dtype=str)
    input_arr = np.array(input_list)[:, [0, 2]]
    input_df = pd.DataFrame(input_arr)
    p1 = input_df.iloc[:, 0].str.split(',', expand=True)
    p2 = input_df.iloc[:, 1].str.split(',', expand=True)
    input_df = pd.concat([p1, p2], axis=1)
    input_df.columns = ['x1', 'y1', 'x2', 'y2']
    input_df = input_df.astype(int)

    return input_df


def part_1(input_df):
    """ Solution to part 1 """
    no_diags = input_df.loc[(input_df['x1'] == input_df['x2']) | (input_df['y1'] == input_df['y2']), :]
    all_points = []
    for i, row in no_diags.iterrows():
        if row['x1'] == row['x2']:
            big_end = max(row['y1'], row['y2'])
            small_end = min(row['y1'], row['y2'])
            for y in range(small_end, big_end + 1):
                all_points.append((row['x1'], y))
        else:
            big_end = max(row['x1'], row['x2'])
            small_end = min(row['x1'], row['x2'])
            for x in range(small_end, big_end + 1):
                all_points.append((x, row['y1']))

    max_ind = max(no_diags.max())
    grid = np.zeros([max_ind + 1, max_ind + 1])
    for point in all_points:
        grid[point] += 1

    unique, counts = np.unique(grid, return_counts=True)
    answer = 0
    for i, num in enumerate(unique):
        if num >= 2:
            answer += counts[i]

    return answer

def part_2(input_df):
    """ Solution to part 2 """
    all_points = []
    for _, row in input_df.iterrows():
        if row['x1'] == row['x2']:
            big_end = max(row['y1'], row['y2'])
            small_end = min(row['y1'], row['y2'])
            for y in range(small_end, big_end + 1):
                all_points.append((row['x1'], y))
        elif row['y1'] == row['y2']:
            big_end = max(row['x1'], row['x2'])
            small_end = min(row['x1'], row['x2'])
            for x in range(small_end, big_end + 1):
                all_points.append((x, row['y1']))
        else:
            big_x = row['x2'] + 1 if row['x2'] > row['x1'] else row['x2'] - 1
            small_x = row['x1']
            x_step = -1 if row['x2'] < row['x1'] else 1
            big_y = row['y2'] + 1 if row['y2'] > row['y1'] else row['y2'] - 1
            small_y = row['y1']
            y_step = -1 if row['y2'] < row['y1'] else 1
            for x, y in zip(range(small_x, big_x, x_step), range(small_y, big_y, y_step)):
                all_points.append((x, y))

    max_ind = max(input_df.max())
    grid = np.zeros([max_ind + 1, max_ind + 1])
    for point in all_points:
        grid[point] += 1

    unique, counts = np.unique(grid, return_counts=True)
    answer = 0
    for i, num in enumerate(unique):
        if num >= 2:
            answer += counts[i]

    return answer


def main():
    """ Test solutions and get answers """
    # Test
    test_input_df = load_inputs('day_5/day_5_test.txt')

    part_1_answer = part_1(test_input_df)
    assert part_1_answer == 5
    print('Part 1 passed test')

    part_2_answer = part_2(test_input_df)
    assert part_2_answer == 12
    print('Part 2 passed test')

    # Run
    input_df = load_inputs('day_5/day_5_inputs.txt')

    part_1_answer = part_1(input_df)
    print('Part 1: ', part_1_answer)

    part_2_answer = part_2(input_df)
    print('Part 2: ', part_2_answer)

if __name__ == '__main__':
    main()
