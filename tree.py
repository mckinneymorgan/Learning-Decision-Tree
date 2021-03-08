# Original author: Morgan McKinney 3/2021

from anytree import *
import math
import copy

"""class Node:
    def __init__(self):
        self.prediction = -1
        self.feature = -1
        self.children = {}"""


def entropy(data):
    feature_column = len(data[0]) - 1
    if feature_column > 44:  # Temporary fix for fluctuating data length
        feature_column = 44
    positive_labels = 0
    negative_labels = 0
    entry = -1
    for x in data:  # Find amount of each label
        entry += 1
        if data[entry][feature_column] == 1:
            positive_labels += 1
        else:
            negative_labels += 1
    # Calculate each pi
    pp = positive_labels / len(data)
    pn = negative_labels / len(data)
    # Entropy calculation
    if pp == 0:
        e = 0 - pn * math.log(pn, 2)
    elif pn == 0:
        e = - pp * math.log(pp, 2) - 0
    else:
        e = - pp * math.log(pp, 2) - pn * math.log(pn, 2)
    return e


def info_gain(data, feature, feature_list):
    sigma = 0
    feature_index = feature_list.index(feature)
    values = [data[0][feature_index]]
    entry = -1
    for x in data:  # Find amount of unique values
        entry += 1
        if data[entry][feature_index] not in values:
            values.append(data[entry][feature_index])
    value_count = [0] * len(values)
    entry = -1
    for x in data:  # Find occurrences of each value
        entry += 1
        value = -1
        for v in values:
            value += 1
            if data[entry][feature_index] == values[value]:
                value_count[value] += 1
    value = -1
    for v in values:  # Calculate sigma
        value += 1
        dv = [x for x in data if x[feature_index] == values[value]]
        sigma += (len(dv) / len(data)) * entropy(dv)
    gain = entropy(data) - sigma
    return gain


def id3(data, features, feature_list):
    # Create a root node for the tree
    feature_column = len(data[0]) - 1
    if feature_column > 44:  # Temporary fix for fluctuating data length
        feature_column = 44
    root = Node("Root", parent=None, prediction=-1, feature=-1, val=-1)
    if root.depth > 0:
        root.name = "Branch"

    # Base cases:
    if all(elements[feature_column] == 1 for elements in data):  # All positive examples
        # Return the single-node tree root with label = +
        root.name = "Leaf"
        root.prediction = 1
        return root
    elif all(elements[feature_column] == 0 for elements in data):  # All negative examples
        # Return the single-node tree root with label =-
        root.name = "Leaf"
        root.prediction = 0
        return root
    elif (not features) or (root.depth >= 3):  # No attributes left to split on or max depth met
        # Return the single-node tree root with label = most common value of target attribute
        root.name = "Leaf"
        positive_labels = 0
        negative_labels = 0
        entry = -1
        for x in data:  # Find most common class label
            entry += 1
            if data[entry][feature_column] == 1:
                positive_labels += 1
            else:
                negative_labels += 1
        if positive_labels >= negative_labels:
            root.prediction = 1
        else:
            root.prediction = 0
        return root
    else:  # Otherwise, begin:
        # Use info gain to select attribute, becomes value of node
        feature_count = len(features)
        gains = []
        index = -1
        for x in range(feature_count):
            index += 1
            gains.append(info_gain(data, features[index], feature_list))
        max_gain = max(gains)
        max_gain_index = gains.index(max_gain)
        print("Info gains:")
        print(gains)

        # Split on feature with highest gain
        print("Feature to split on:")
        print(max_gain_index)
        root.feature = max_gain_index

        # Find amount and frequencies of each value for feature
        feature_index = feature_list.index(features[max_gain_index])
        values = []
        entry = -1
        for x in data:  # Find amount of unique values
            entry += 1
            if entry == 0:
                values.append(data[entry][feature_index])
            else:
                if data[entry][feature_index] not in values:
                    values.append(data[entry][feature_index])
        value_count = [0] * len(values)
        entry = -1
        for x in data:  # Find occurrences of each value
            entry += 1
            value = -1
            for v in values:
                value += 1
                if data[entry][feature_index] == values[value]:
                    value_count[value] += 1

        # For each value in attribute add children
        value = -1
        for v in values:
            # Add new tree branch below root for value(s) A=vi
            value += 1

            # Let examples(vi) be subset of examples that have value vi for A
            # Get subset of data where attribute A=vi -- divide data into subsets
            partitioned_data = [x for x in data if x[feature_index] == values[value]]

            # If examples(vi) is empty
            if not partitioned_data:
                # Child becomes leaf, create leaf (majority class label)
                leaf = Node("Leaf", parent=root, prediction=-1, feature=feature_index, val=values[value])
                positive_labels = 0
                negative_labels = 0
                entry = -1
                for x in data:  # Find most common class label
                    entry += 1
                    if data[entry][feature_index] == 1:
                        positive_labels += 1
                    else:
                        negative_labels += 1
                if positive_labels >= negative_labels:
                    leaf.prediction = 1
                else:
                    leaf.prediction = 0
            # Else below this branch add subtree ID3(examples(vi), class label, attributes-{A})
            else:
                # Make recursive call with subset of data and attributes list without current attribute
                # Referenced: Jainam helped clarify AnyTree syntax for recursion
                feature_subset = copy.deepcopy(features)
                element = features[max_gain_index]
                feature_subset = [x for x in feature_subset if x != element]
                branch = id3(partitioned_data, feature_subset, feature_list)
                branch.parent = root
                branch.val = values[value]
                # Note: Attributes can be reused if on different subtrees
                # Important: Scope of attributes-{A} pass by copy not by reference
    return root
