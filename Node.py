class Node:

    # Constructor
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None


    # Set data of the Node
    def setData(self, data):
        self.data = data

    # Get data of the node
    def getData (self):
        return self.data

    # Set next of the Node
    def setNext (self, next):
        self.next = next

    # Get next of the node
    def getNext (self):
        return self.next

    # Set previous of the node
    def setPrev (self, prev):
        self.prev = prev

    # Get previous of the node
    def getPrev (self):
        return self.prev

    # Get if has a next
    def hasNext (self):
        return self.next is not None

    # Get if has a previous
    def hasPrev(self):
        return self.prev is not None