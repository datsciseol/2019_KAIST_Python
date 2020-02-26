class Node:
    def __init__(self, objValue = "", nextNode = "", binHead = False, binTail = False):
        self.objValue = objValue
        self.nextNode = nextNode
        self.binHead = binHead
        self.binTail = binTail
    def getNext(self):
        return self.nextNode
    def getValue(self):
        return self.objValue
    def setNext(self, node):
        self.nextNode = node
    def setValue(self, objValue):
        self.objValue = objValue
    def isHead(self):
        return self.binHead
    def isTail(self):
        return self.binTail

class SingleLinkedList:
    self.nodeTail = Node(binTail = True)
    self.nodeHead = Node(binHead = True)
    self.size = 0
    def insertAt(self, insertVal, insertIdx):
        nodeInsert = Node(objValue = insertVal)
        nodePrev = self.get(insertIdx - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeInsert)
        nodeInsert.setNext(nodeNext)
        self.size += 1
    def removeAt(self, removeIdx):
        nodePrev = self.get(removeIdx - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size -= 1
    def get(self, retrieveIdx):
        node = self.nodeHead
        for iter in range(retrieveIdex + 1):
            node = node.getNext()
        return node
    def getSize(self):
        return self.size
    def printStatus(self):
        node = self.nodeHead
        while node.getNext().isTail() != False:
            node = node.getNext()
            print(node.getValue(), end = " ")
        print()

class Stack:
    stack = SingleLinkedList()
    def push(self, num):
        self.stack.insertAt(num, 0)
    def pop(self):
        self.stack.removeAt(0)

class Queue:
    queue = SingleLinkedList()
    def enqueue(self, num):
        self.queue.insertAt(num, self.getSize())
    def dequeue(self):
        self.queue.removeAt(0)

