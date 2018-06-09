# Крускал алгоритм |
# сортировка O(E * logE)
# + выбор из набора [O(E * a(E, V)) ~ const] = O(E * logE)

# нужно простроить минимальное островное дерево:
# 1. сортируем все грани графа по возрастания
# 2. берем наименьшую грань и проверяем, что эти две вершины
# находятся в разных disjointSet, если в разных, то соединяем
# эти вершины в один набор (disjointSet), если в одном наборе, то
# нельзя соединять, так как будет цикл!
#  2.1 при этом соединяем
# не просто так, а мы проверяем какая из disjointSet имеет
# наибольшую высоту, вот к ней и присоединяем другой набор
# 3. проходимся по всем граням и потом - конец алгоритма

# Крускал применяют для не полносвязных вершин, когда сортировка
# граней будет достаточно быстрой и не нужно применять heap
# если полносвязный граф, то нужно применять алгоритм Прима, он
# быстрее будет работать, но при этом требует дополнительные
# O(E) памяти!

class Vertex(object):

  def __init__(self, name):
    self.name = name
    self.node = None # disjoint set for this Vertex ???


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
    while currentNode.parentNode is not None:
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


  def merge(self, node1, node2): # соединяем два disjointSet в один

    # ищем representative - nodeId для наборов node1 / node2
    index1 = self.find(node1)
    index2 = self.find(node2)

    if index1 == index2:
      return ; # node1 and node2 in the same set - dont merget them!


    root1 = self.rootNodes[index1]
    root2 = self.rootNodes[index2]

    # проверяем, какой set к кому лучше присоединить
    if root1.height < root2.height: # 1 < 2 => 2 - representative
      root1.parentNode = root2
    elif root1.height > root2.height: # 1 > 2 => 1 - representative
      root2.parentNode = root1
    else:
      root2.parentNode = root1 # 1 = 2 => 1 - representative / H++
      root1.height += 1 # высота root1 поддерева увеличилась 1 ++

  def makeSets(self, vertexList):
    for v in vertexList:
      self.makeSet(v)

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


class KruskalAlgorithm(object):

  def spanningTree(self, vertexList, edgeList):
    # создаем disjointSet для каждой веришны
    disjointSet = DisjointSet(vertexList)
    # минимальное spanning tree (островное дерево)
    spanningTree = []

    edgeList.sort() # сортируем все грани по весу __cmp__

    for edge in edgeList:

      # вытаскиваем начальную и конечную вершины
      start = edge.startVertex
      end = edge.targetVertex

      # если вершины грани принадлежат разным disjointSet => merge
      if disjointSet.find(start.node) is not disjointSet.find(end.node):
        spanningTree.append(edge) # добавляем грань в островное дерево
        disjointSet.merge(start.node, end.node) # соединяем сэты

    # вывод результата
    for edge in spanningTree:
      print(edge.startVertex.name, " - ", edge.targetVertex.name)


vertex1 = Vertex('a')
vertex2 = Vertex('b')
vertex3 = Vertex('c')
vertex4 = Vertex('d')
vertex5 = Vertex('e')
vertex6 = Vertex('f')
vertex7 = Vertex('g')

edge1 = Edge(2 ,vertex1 ,vertex2)
edge2 = Edge(6 ,vertex1 ,vertex3)
edge3 = Edge(5 ,vertex1 ,vertex5)
edge4 = Edge(10 ,vertex1 ,vertex6)
edge5 = Edge(3 ,vertex2 ,vertex4)
edge6 = Edge(3 ,vertex2 ,vertex5)
edge7 = Edge(1 ,vertex3 ,vertex4)
edge8 = Edge(2 ,vertex3 ,vertex6)
edge9 = Edge(4 ,vertex4 ,vertex5)
edge10 = Edge(5 ,vertex4 ,vertex7)
edge11 = Edge(5 ,vertex6 ,vertex7)

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)
vertexList.append(vertex7)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)
edgeList.append(edge11)

algorithm = KruskalAlgorithm()
algorithm.spanningTree(vertexList, edgeList)

