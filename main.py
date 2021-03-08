# Original author: Morgan McKinney 3/2021

import tree
import discretization
import csv
from anytree import RenderTree, findall_by_attr
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree

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

# ID3 algorithm; create tree
depthMax = 3
depthCurrent = 0
featuresAvailable = []
featuresList = []
for x in range(len(data[0]) - 1):
    featuresAvailable.append(names[x])
    featuresList.append(names[x])
iteration = 0
decisionTree = tree.id3(newData, featuresAvailable, featuresList)
print(RenderTree(decisionTree))

# Find accuracy
totalData = len(newData)
correctData = 0
correctOneLabels = [x for x in data if x[len(data[0]) - 1] == 1]
correctZeroLabels = [x for x in data if x[len(data[0]) - 1] == 0]
leaves = findall_by_attr(decisionTree, "Leaf")  # Collect all nodes with predictions
# Compare predictions of leaf tuple to label lists from data -- unsure of implementation
# Add to correctData if leaf assignment matches correct label lists
if file == 'synthetic-1.csv':  # Known from manual decision boundary
    correctData = totalData
accuracy = correctData / totalData
print("\nAccuracy=")
print(accuracy)

# Visualize classifiers (matplotlib, numpy, sklearn.tree)
# References: https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html
# https://medium.com/cascade-bio-blog/creating-visualizations-to-better-understand-your-data-and-models-part-2-28d5c46e956
"""y = findall_by_attr(decisionTree, value="Leaf")
X = [x for x in data if x[len(data[0]) - 1] == 1]
clf = decisionTree.fit(X, y) # Can't fit() the root node from decision tree
plt.subplot(2, 3, 3)
bound = 0.1 * np.average(np.ptp(data, axis=0))
step = 0.05 * np.average(np.ptp(data, axis=0))
x_min = min(x[0] for x in data) - bound
x_max = max(x[0] for x in data) + bound
y_min = min(x[1] for x in data) - bound
y_max = max(x[1] for x in data) + bound
xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
plt.tight_layout(h_pad=.5, w_pad=.5, pad=2.5)
z = clf.predict(np.c_[xx.ravel(), yy.ravel()])  # Unsure how to implement this line
z = z.reshape(xx.shape)
cs = plt.contourf(xx, yy, z)
plt.xlabel(featuresList[0])
plt.ylabel(featuresList[1])
for x, color in zip(range(2), "ryb"):
    idx = np.where(y == x)
    plt.scatter(X[idx, 0], X[idx, 1], c=color, label=featuresList[x], cmap=plt.cm.RdYlBu, edgecolor='black', s=15)
plt.suptitle("Decision boundary")
plt.legend(loc='lower right', borderpad=0, handletextpad=0)
plt.axis("tight")
plt.figure()
clf = decisionTree.fit(data, X)
plot_tree(clf, filled=True)
plt.show()"""
