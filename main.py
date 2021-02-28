# Original author: Morgan McKinney

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv

# User input, get filename(s)
print("MACHINE LEARNING DECISION TREE \n")
file = input("Enter csv file name: ")
classLabelFile = input("Are the class labels in another file (Y/N): ")
if classLabelFile.lower() == 'y':
    classLabelFile = input("Enter class label file name: ")

features = []
classLabel = []
featureNames = False
if file == 'pokemonStats.csv':
    featureNames = True
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    if featureNames:
        for row in readCSV:

            print(row)

# Discretize data
    # Call script; create new version of data set
    # Discretize both features

# ID3(data, class label, available attributes to split on)
    # Create a root node for the tree
    # Base cases:
    # If all examples are positive
        # return the single-node tree root with label =+
    # If all examples are negative
        # return the single-node tree root with label =-
    # No attributes left to split on
        # return the single-node tree root with label =most common value of target attribute
    # Otherwise, begin:
        # Use info gain to select attribute, becomes value of node
        # Info gain(data, attribute) = entropy(data)-[avg. entropy of subsets by splitting on A]
        # G(D,A)=E(D)-sigma of v exists in values(A)[|Dv|/|D| * E(Dv)]
        # Entropy(data) = -sigma of i[Pi * log base 2(Pi)]
        # Pi = # samples of class i in data / # samples in data
        # Split on feature with highest gain
        # Construct node for attribute or assign to node
        # For each value in attribute add children
            # Add new tree branch below root for value(s) A=vi

            # Let examples(vi) be subset of examples that have value vi for A
            # Get subset of data where attribute A=vi -- divide data into subsets

            # If examples(vi) is empty
            # No examples where A=vi -> child becomes leaf, create leaf (majority class label)

            # Else below this branch add subtree ID3(examples(vi), class label, attributes-{A})
            # Make recursive call with subset of data and attributes list without current attribute
            # Note: Attributes can be reused if on different subtrees
            # Important: Scope of attributes-{A} pass by copy not by reference
    # End
    # Return root

# Visualize classifiers (matplotlib)

print("\nComplete.")