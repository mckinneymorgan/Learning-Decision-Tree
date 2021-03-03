# Original author: Morgan McKinney

def equidistant_bins(data, features, bin_num):
    new_data = []
    min_list = []
    width_list = []
    feature_count = -1
    for x in features:  # For every feature
        # Determine feature value range
        feature_count += 1
        feature_name = 'feature' + str(x)
        max_value = max(item[feature_name] for item in data)
        min_value = min(item[feature_name] for item in data)
        min_list.append(min_value)
        value_range = max_value - min_value

        # Determine bin width for feature
        width = value_range / bin_num
        width_list.append(width)

    for x in data:  # For every entry
        row_dict = dict(id=x)
        for y in features:  # For every feature
            # Assign values to bins
            bin_min = min_list[y]
            bin_max = min_list[y]
            for z in bin_num:  # For every bin
                # Find all values in range of bin
                for key, value in data[x].items():
                    if bin_min <= int(value) <= bin_max:
                        result[key] = value
                # Reassign values into bin
        new_data.append(row_dict)

    print("Discretized:")
    print(new_data)
    return new_data
