# Original author: Morgan McKinney

def equidistant_bins(data, bin_num):
    new_data = []
    for x in data:  # For every feature
        new_data.append([])

        # Determine feature range
        max_value = max(data[x], key=data[x].get)
        min_value = min(data[x], key=data[x].get)
        value_range = max_value - min_value

        # Determine bin width
        width = value_range/bin_num

        # Assign values to bins
        for y in bin_num:  # For every bin
            bin_min = min_value + width*y
            bin_max = min_value + width*(y+1)
            bin_value = bin_max - bin_min
            result = dict()
            # Find all values in range of bin
            for key, value in data[x].items():
                if bin_min <= int(value) <= bin_max:
                    result[key] = value
            # Reassign values into bin

            new_data[x].append(dict)

    print("Discrete data: ")
    print(new_data)
    return new_data
