# Original author: Morgan McKinney 3/2021

import math


def equidistant_bins(data, bin_num):
    new_data = []
    min_list = []
    width_list = []
    feature_count = len(data[0])-1
    for x in range(feature_count):  # For every feature
        # Determine feature value range
        max_value = max(y[x] for y in data)
        min_value = min(y[x] for y in data)
        max_value = math.ceil(max_value)
        min_value = math.floor(min_value)
        min_list.append(min_value)
        value_range = max_value - min_value

        # Determine bin width for feature
        width = value_range / bin_num
        width = math.ceil(width)
        width_list.append(width)
    print("Width list, min. value list: ")
    print(width_list)
    print(min_list)
    entry = -1
    for x in data:  # For every entry
        entry += 1
        new_row = []
        feature = 0
        for y in range(feature_count):  # For every feature
            feature += 1
            if feature >= 8:  # Don't bin past feature 8, binary binning causes problems
                new_row.append(int(data[entry][y]))
            else:  # Assign values to bins
                bin_max = min_list[y] + width_list[y]
                bin_min = min_list[y]
                bin_val = math.ceil(bin_min + width_list[y]/2)
                for z in range(bin_num):  # For every bin
                    # Reassign value into bin if it fits
                    if (bin_min <= data[entry][y] <= bin_max) and (feature < 8):
                        new_row.append(bin_val)
                    # Adjust local bin max and min
                    bin_max += width_list[y]
                    bin_min += width_list[y]
                    bin_val += width_list[y]
        new_row.append(data[entry][feature_count])  # Add class labels back
        new_data.append(new_row)
    return new_data
