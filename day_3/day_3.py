import numpy as np
from pathlib import Path

def load_inputs(input_path):
    """ Load inputs from txt file """
    input_list = np.loadtxt(Path(input_path), dtype=str)
    input_list = [[char for char in binary] for binary in input_list]
    input_arr = np.array(input_list, dtype=int)

    return input_arr

def most_least(arr):
    """ Find most and least common values for each bit position """
    half = arr.shape[0] / 2
    input_sum = np.sum(arr, axis=0)
    most_common = ''
    least_common = ''
    for ind in input_sum:
        if ind >= half:
            most_common += '1'
            least_common += '0'
        else:
            most_common += '0'
            least_common += '1'
    return most_common, least_common

def part_1(input_arr):
    """ Solution to part 1 """
    gamma, epsilon = most_least(input_arr)
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    answer = gamma * epsilon

    return answer

def part_2(input_arr):
    """ Solution to part 2 """
    oxy_arr = input_arr.copy()
    for ind in range(input_arr.shape[1]):
        if oxy_arr.shape[0] == 1:
            continue
        most, _ = most_least(oxy_arr)
        bool_filt = oxy_arr[:, ind] == int(most[ind])
        oxy_arr = oxy_arr[bool_filt, :]

    co2_arr = input_arr.copy()
    for ind in range(input_arr.shape[1]):
        if co2_arr.shape[0] == 1:
            continue
        _, least = most_least(co2_arr)
        bool_filt = co2_arr[:, ind] == int(least[ind])
        co2_arr = co2_arr[bool_filt, :]

    oxy_str = ''.join(oxy_arr[0].astype(str))
    co2_str = ''.join(co2_arr[0].astype(str))
    oxy = int(oxy_str, 2)
    co2 = int(co2_str, 2)
    answer = oxy * co2

    return answer


def main():
    """ Test solutions and get answers """
    # Test
    test_input_arr = load_inputs('day_3/day_3_test.txt')

    part_1_answer = part_1(test_input_arr)
    assert part_1_answer == 198
    print('Part 1 passed test')

    part_2_answer = part_2(test_input_arr)
    assert part_2_answer == 230
    print('Part 2 passed test')

    # Run
    input_arr = load_inputs('day_3/day_3_inputs.txt')

    part_1_answer = part_1(input_arr)
    print('Part 1: ', part_1_answer)

    part_2_answer = part_2(input_arr)
    print('Part 2: ', part_2_answer)

if __name__ == '__main__':
    main()
