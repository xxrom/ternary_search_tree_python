class Node(object):

  def __init__(self, character):
    self.character = character
    self.leftNode = None
    self.middleNode = None
    self.rightNode = None
    self.value = 0

class TernarySearchTree(object):

  def __init__(self):
    self.root = None

  def put(self, key, value):
    self.root = self.putItem(self.root, key, value, 0)

  def putItem(self, node, key, value, index): # key[index] - path
    char = key[index]

    if node == None: # создаем новую ноду
      node = Node(char)

    if char < node.character: # меньше => left
      node.leftNode = self.putItem(
        node.leftNode,
        key,
        value,
        index # не повышаем индекс, т.к. левый ребенок и тот же уровень
      )
    elif char > node.character: # больше => right
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
      node.value = value # сохраняем value значение

    return node

  def get(self, key):
    node = self.getItem(self.root, key, 0)

    if node == None:
      return -1 # не нашли значение !

    return node.value # значит нашли значение

  def getItem(self, node, key, index):
    char = key[index]

    if node == None:
      return None # не нашли нужное значение

    if node.character == char and index < len(key) - 1 : # совпадает значение
      # увеличиваем index только в middle!!!
      return self.getItem(node.middleNode, key, index + 1)

    if char > node.character: # справа смотрим ребенка
      return self.getItem(node.rightNode, key, index)

    if char < node.character: # смотрим справа
      return self.getItem(node.leftNode, key, index)

    return node # нашли значение


if __name__ == '__main__':
  tst = TernarySearchTree()

  tst.put('apple', 100)
  tst.put('apper', 1001)
  tst.put('appeturme', 10201)
  tst.put('orange', 200)

  print(tst.get('apple'))
  print(tst.get('apper'))
  print(tst.get('orange'))
  print(tst.get('appeturme'))