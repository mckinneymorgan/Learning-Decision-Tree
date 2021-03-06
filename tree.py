# Original author: Morgan McKinney 3/2021

from anytree import *


"""class Node:
    def __init__(self):
        self.prediction = -1
        self.feature = -1
        self.children = {}"""


def info_gain(data, feature):
    gain = 0
    return gain


# Info gain(data, attribute) = entropy(data)-[avg. entropy of subsets by splitting on A]
# G(D,A)=E(D)-sigma of v exists in values(A)[|Dv|/|D| * E(Dv)]
# Entropy(data) = -sigma of i[Pi * log base 2(Pi)]
# Pi = # samples of class i in data / # samples in data

def id3(data, features, depth):
    feature_column = len(data[0])-1
    # Create a root node for the tree
    root = Node("root", prediction=-1, feature=-1)
    # Base cases:
    if all(elements == data[0][feature_column] for elements in data): # All positive examples
        # Return the single-node tree root with label = +
        root.prediction = 1
        return root
    elif all(elements == data[0][feature_column] for elements in data): # All negative examples
        # Return the single-node tree root with label =-
        root.prediction = 0
        return root
    elif not features or depth >= 3: # No attributes left to split on or max depth met
        # Return the single-node tree root with label = most common value of target attribute
        positive_labels = 0
        negative_labels = 0
        for x in data:  # Find most common class label
            if data[x][feature_column] == 1:
                positive_labels += 1
            else:
                negative_labels += 1
        if positive_labels >= negative_labels:
            root.prediction = 1
        else:
            root.prediction = 0
        return root
    else: # Otherwise, begin:
        feature_count = len(features)
        # Use info gain to select attribute, becomes value of node
        gains = [0] * feature_count
        for x in range(feature_count):
            gains[x] = info_gain(data, x)
        max_gain = max(gains)
        # Split on feature with highest gain
        # Construct node for attribute or assign to node
        # For each value in attribute add children
        # Add new tree branch below root for value(s) A=vi

        # Let examples(vi) be subset of examples that have value vi for A
        # Get subset of data where attribute A=vi -- divide data into subsets
        # Notes:
        # partitionedData = [x for x in data if x[bestFeature] == split]

        # If examples(vi) is empty
        # No examples where A=vi -> child becomes leaf, create leaf (majority class label)

        # Else below this branch add subtree ID3(examples(vi), class label, attributes-{A})
        # Make recursive call with subset of data and attributes list without current attribute
        # Note: Attributes can be reused if on different subtrees
        # Important: Scope of attributes-{A} pass by copy not by reference
    # End
    return root
