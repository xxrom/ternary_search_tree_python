class Node(object):

  def __init__(self, character):
    self.character = character
    self.leftNode = None
    self.middleNode = None
    self.rightNode = None
    self.value = 0

class TernarySearchTree(object):

  def __init__(self):
    self.rootNode = None

  def put(self, key, value):
    self.rootNode = self.putItem(self.rootNode, key, value, 0)

  def putItem(self, node, key, value, index): # key[index] - path
    char = key[index]

    if node == None: # создаем новую ноду
      node = Node(char)

    if char < node.character: #
      node.leftNode = self.putItem(
        node.leftNode,
        key,
        value,
        index # не повышаем индекс, т.к. левый ребенок и тот же уровень
      )
    elif char > node.character:
      node.rightNode = self.putItem(
        node.rightNode,
        key,
        value,
        index # same level in the tree
      )
    elif index < len(key) - 1: # not the last index in the key
      node.middleNode = self.putItem(
        node.middleNode,
        key,
        value,
        index + 1 # спустились на уровень ниже посередине
      )
    else: # last index in the key
      node.value = value # сохраняем новое значение


