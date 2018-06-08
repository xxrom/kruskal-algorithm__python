class Vertex(object):

  def __init__(self, name):
    self.name = name
    self.node = node # disjoint set for this Vertex ???


class Node(object): # disjoint set ???

  def __init__(self, height, nodeId, parentNode):
    self.height = height
    self.nodeId = nodeId
    self.parentNode = parentNode

class Edge(object):

  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex

  def __cmp__(self, otherEdge): # сравнивать грани нужно по весам!!!
    return self.cmp(self.weight, self.weight)

  def __lt__(self, other):
    selfPriority = self.weight
    otherPriority = other.weight
    return selfPriority < otherPriority

class DisjointSet(object):