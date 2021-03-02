# Original author: Morgan McKinney

import anytree
import discretization
import csv

# User input, get filename(s)
print("MACHINE LEARNING DECISION TREE \n")
file = input("Enter csv file name: ")
classLabelFileExist = False
classLabelFile = input("Are the class labels in another file (Y/N): ")
if classLabelFile.lower() == 'y':
    classLabelFile = input("Enter class label file name: ")
    classLabelFileExist = True
featureNames = False
featureNamesExist = input("Are the features named (Y/N): ")
if featureNamesExist.lower() == 'y':
    featureNames = True

names = []
data = []
classLabelName = '0'
classLabels = []
# Read file
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # Count features, return to start of file
    featureCount = len(next(readCSV))
    if not classLabelFileExist:
        featureCount -= 1
    csvfile.seek(0)
    print("Feature count: ")
    print(featureCount)

    # Create data list of lists
    for x in range(featureCount):
        data.append([])
    print("Empty data list: ")
    print(data)

    # Name features, if provided
    if featureNames:
        names = next(readCSV)
        if not classLabelFileExist:
            names.pop()
        csvfile.seek(0)
    else:
        for x in range(featureCount):
            names.append(x)
    print("Names: ")
    print(names)

    # Populate data list
    for row in readCSV:
        for x in range(featureCount):
            data[x].append(dict(name=names[x], value=row[x]))
    print("Populated data list: ")
    print(data)

    # Populate class list
    if not classLabelFileExist:
        csvfile.seek(0)
        for row in readCSV:
            classLabels.append(row[featureCount])

# Open class label file if applicable
if classLabelFileExist:
    with open(classLabelFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # Populate class list
        if featureNamesExist:
            classLabelName = next(readCSV)
        for row in readCSV:
            classLabels.append(row[0])

print("Class label name: ")
print(classLabelName)
print("Class labels: ")
print(classLabels)

# Discretize data; create new version of data set
discretizedData = discretization.equidistantbins(data)
# Discretize all features

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
