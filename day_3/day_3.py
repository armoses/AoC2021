import numpy as np
from pathlib import Path

def most_least(arr):
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

def main(input_path):
    with input_path as f:
        input_list = np.loadtxt(f, dtype=str)
    input_list = [[char for char in binary] for binary in input_list]
    input_arr = np.array(input_list, dtype=int)

    # Part 1
    gamma, epsilon = most_least(input_arr)
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    print('Part 1: ', gamma * epsilon)

    # Part 2
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
    print('Part 2: ', oxy * co2)

if __name__ == '__main__':
    input_path = Path('day_3/day_3_inputs.txt')
    main(input_path)
