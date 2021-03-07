# Original author: Morgan McKinney 3/2021

from anytree import *
import tree
import discretization
import csv
import copy

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

# Read file
names = []
data = []
classLabelName = 0
classLabels = []
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # Count features, return to start of file
    featureCount = len(next(readCSV))
    if not classLabelFileExist:
        featureCount -= 1
    csvfile.seek(0)
    print("\nFeature count: ")
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

# Discretize data; create new version of data set
binNum = 5
newData = discretization.equidistant_bins(data, binNum)
newDataCopy = copy.deepcopy(newData)

# ID3 algorithm; create tree
depthMax = 3
depthCurrent = 0
featuresAvailable = []
featuresList = []
for x in range(len(data[0])-1):
    featuresAvailable.append(names[x])
    featuresList.append(names[x])
iteration = 0
decisionTree = tree.id3(newDataCopy, featuresAvailable, featuresList, depthCurrent, iteration)
print(RenderTree(decisionTree))

# Visualize classifiers (matplotlib)
