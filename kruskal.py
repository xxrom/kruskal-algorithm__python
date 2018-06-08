class Vertex(object):

  def __init__(self, name):
    self.name = name
    self.node = node # disjoint set for this Vertex ???


class Node(object): # disjoint set ???

  def __init__(self, height, nodeId, parentNode):
    self.height = height
    self.nodeId = nodeId
    self.parentNode = parentNode


class Edge(object): # грань, сравнение и

  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex

  # перегрузка оператора сравнения
  def __cmp__(self, otherEdge): # сравнивать грани нужно по весам!!!
    return self.cmp(self.weight, self.weight)

  # перегрузка оператора меньше <
  def __lt__(self, other): # less then <
    selfPriority = self.weight
    otherPriority = other.weight
    return selfPriority < otherPriority


class DisjointSet(object):

  def __init__(self, vertexList):
    self.vertexList = vertexList
    self.rootNodes = []
    self.nodeCount = 0
    self.setCount = 0 # number of disjoint sets with nodes
    self.makeSets(vertexList)


  # соединяем node на прямую к корню данного disjoint set
  def find(self, node):
    currentNode = node

    # ищем root node
    while currentNode.parentNode in not None:
      currentNode = currentNode.parentNode

    # нашли root
    root = currentNode
    # вернули начальную node
    currentNode = node

    # все вершины по пути к root прямиком в root соединяем !!! =)
    while currentNode is not root:
      temp = currentNode.parentNode
      currentNode.parentNode = root
      currentNode = temp

    # вернем идентификатор для данного disjoint set
    return root.nodeId


  def merge(self, node1, node2):

    index1 = self.find(node1)
    index2 = self.find(node2)

    if index1 == index2:
      return ; # node1 and node2 in the same set - dont merget them!

    root1 = self.rootNodes[index1]
    root2 = self.rootNodes[index2]

    if root1.height < root2.height:
      root1.parentNode = root2
    elif root1.height > root2.height:
      root2.parentNode = root1
      root1.height += 1 # высота root1 поддерева увеличилась 1???

  def makeSets(self, vertexList):
    for v in vertexList:
      slef.makeSets(v)

  def makeSet(self, vertex):
    node = Node(
      0, # height for this node
      len(self.rootNodes), # nodeId ??? l104
      None # parent node
    )
    vertex.node = node
    self.rootNodes.append(node)
    self.setCount = self.setCount + 1
    self.nodeCount = self.nodeCount + 1

