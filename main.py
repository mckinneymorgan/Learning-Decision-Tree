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

# Notes:
# file = open("file.txt", "r")
    # lines = file.readlines()
    # lines = lines.rstrip("\n")
    # lines = lines.split(",")
    # lines[0]
    # lines[0][1]
# partitionedData = [x for x in data if x[bestFeature] == split]

names = []
data = []
classLabelName = 0
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

    # Name features, if provided
    if featureNames:
        names = next(readCSV)
        if not classLabelFileExist:
            names.pop()
    else:
        for x in range(featureCount):
            names.append(x)
    print("Names: ")
    print(names)

    # Populate data list
    for row in readCSV:
        rowList = []
        for x in range(featureCount):
            rowEntry = float(row[x])
            rowList.append(rowEntry)
        data.append(rowList)

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

# Append class labels to data set
entry = -1
for x in data:
    entry += 1
    classLabel = classLabels[entry]
    if classLabel == 'True':
        classLabel = 1
    elif classLabel == 'False':
        classLabel = 0
    else:
        classLabel = int(classLabel)
    data[entry].append(classLabel)
print("Data with labels: ")
print(data)

# Discretize data; create new version of data set
binNum = 5
newData = discretization.equidistant_bins(data, binNum)

# ID3(data, class label, available attributes to split on, depth)
# Create a root node for the tree
# Base cases:
# If all examples are positive
# return the single-node tree root with label =+
# If all examples are negative
# return the single-node tree root with label =-
# No attributes left to split on
# return the single-node tree root with label =most common value of target attribute
# Max depth met
# Create leaf
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
