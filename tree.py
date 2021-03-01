# Original author: Morgan McKinney

import anytree


class Node:
    def __init__(self, featureID):
        self.featureID = featureID
        self.featureColumn = -1
        self.predictionValue = -1
        self.children = {}
