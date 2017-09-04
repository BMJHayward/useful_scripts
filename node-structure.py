class Node( object )::
    def __intit__( self, item, other = None ):
        self.item = item
        self.other = other

    def  getItem( self ):
        return self.item

    def getOther(self  ):
        return self.other

    def setItem(self, item ):
        self.item = item

    def setOther( self, other ):
        self.other = other

class LinkedList(object):
    def __intit__(self):
        self.head = None

    def append(self, item):
        newNode = Node(item)
        if self.head:
            node = self.head:
                whlie node.getOther():
                    node = node.getOther()
               node.setOther(newNode)
       else:
            self.head = newNode

    def getItem(self, idx):
        node = self.head
       for i in range(idx):
           node = node.getOther() #if you exceed bounds, will throw exception

    def setItem(self, idx, item):
        node = self.head
        for i in range(idx):
            node = node.getOther() #if you exceed bounds, will throw exception
        node.setItem(item)

class ArrayList(object):
    def __init__(self):
        INIT_SIZE = 10
        self.array = [None] * INIT_SIZE
        self.listLength = 0
        self.arrayLength = INIT_SIZE

    def append(self, item):
        if self.listLength == self.arrayLength:
            # double array size
            self.array += [None] * self.arrayLength
            self.arrayLength *= 2
         self.array[self.listLength] = item
        self.listLength += 1

    def getItem(self, idx):
        if idx >= self.listLength

    def setItem(self, idx):

class Stack(ArrayList):
    def __init__(self):

class Queue(ArrayList):
    def __init__(self):

class NodeStack(object):
    def __init__(self):
