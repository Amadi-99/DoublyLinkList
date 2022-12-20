from Node import Node


class DoublyLinkedList:
    # constructor
    def __init__(self):

        self.head = Node()
        self.head = None
        self.length = 1

# Count length of Doubly Link List

    def ListLenght(self):
        current = self.head                 # Assign head as current
        count = 0

        # Count the nodes using while loop
        while current is not None:
            count = count + 1               # Count the nodes
            current = current.getNext()     # Get next node relevant to the current
        return count

# print Doubly Link List

    def printList(self):
        if self.head is None:               # Find the list is empty
            print("Empty Link List")
        else:
            current = self.head             # Assign head as current
            # Go to the forward using while loop to get data
            while current is not None:
                print(current.getData())        # Get the data of  current node
                current = current.getNext()     # Get next node relevant to the current

# Traversing forward and backward methods of the Doubly Link List

    # Traversing forward
    def printListForward(self):

        if self.head is None:                   # Find the list is empty
            print("Empty Link List")
        else:
            current = self.head                 # Assign head as current

            # Go to the forward using while loop to get data
            while current is not None:
                print(current.getData())        # Get the data of  current node
                current = current.getNext()     # Get next node relevant to the current

    # Traversing backward
    def printListReverse(self):

        if self.head is None:                   # Find the list is empty
            print("Empty Link List")
        else:
            current = self.head                 # Assign head as current

            # Go to the forward using while loop to find last node
            while current.getNext() is not None:
                current = current.getNext()     # Get next node relevant to the current

            # Go to the backward using while loop to get data
            while current is not None:
                print(current.getData())        # Get the data of  current node
                current = current.getPrev()     # Get previous node relevant to the current


# Insert the data for beginning,end and given position

    # Insert a node at the beginning of the list

    def addNodeBeginning(self, data):
        # Allocate the node and put in the data
        newNode = Node()
        newNode.setData(data)

        if self.head is None:       # find the first node is none
            self.head = newNode     # Make new node as head
        else:
            newNode.setNext(self.head)      # New node's set next point to head node
            self.head.setPrev(newNode)      # Head node's set previous point to new node
            self.head = newNode             # New node assign to the head
        self.length += 1

    # Insert a node at the end of the list

    def addNodeEnd(self, data):
        # Allocate the node and put in the data
        newNode = Node()
        newNode.setData(data)

        if self.head is None:       # find the first node is none
            self.head = newNode     # Make new node as head
        else:
            current = self.head     # Assign head as current
            # Go to the forward using while loop to find last node
            while current.getNext() is not None:
                current = current.getNext()     # Get next node relevant to the current
            current.setNext(newNode)        # Current node's set next point to new node
            newNode.setPrev(current)        # New node's set previous point to current node
            newNode.setNext(None)           # New node's set next assign to none
        self.length += 1

    # Insert a node at the given position of the list

    def addNodeInPos(self, pos, data):
        # Check the given position in between the list
        if pos > self.length - 1 or pos < 0:    # If given position is not between the list, do nothing ( return none)
            return None
        elif pos == 0:                          # Check the given position is equal to the zero (head position)
            self.addNodeBeginning(data)         # If given position is equal to the zero add the node to beginning
        elif pos == self.length - 1:            # Check the given position is equal to length-1 (last node position)
            self.addNodeEnd(data)               # If given position is equal to the length-1 add the node to end
        else:
            # Allocate the node and put in the data
            newNode = Node()
            newNode.setData(data)
            count = 0
            current = self.head                 # Assign head as current

            # Go to the forward using while loop to find given node
            while count != pos - 1:
                count += 1
                current = current.getNext()     # Get next node relevant to the current

            nextNode = current.getNext()        # Get next node of the current node
            newNode.setNext(nextNode)           # New node's set next point to the next node of the current node
            current.setNext(newNode)            # Current node's set next point to new node
            newNode.setPrev(current)            # New node's set previous point to current node
            nextNode.setPrev(newNode)           # next node of the current node's set previous point to new node


# Delete the data in beginning,end and given position

    # Delete a node at the beginning of the list

    def deleteFirstNode(self):

        if self.head is None:                   # Check the list is empty
            print("Empty link list")

        if self.head.getNext is None:           # check the list has one element
            self.head = None                    # Delete first node
        else:
            self.head = self.head.getNext()     # Get the next node of the head node as head
            current = self.head                 # Assign the head node as current
            previous = current                  # Assign the current as previous
            previous.setPrev(None)              # current node's set previous assign to the none
        self.length -= 1

    # Delete a node at the end of the list

    def deleteLastNode(self):

        if self.head is None:                   # Check the list is empty
            print("Empty link list")

        if self.head.getNext is None:           # Check the list has one element
            self.head = None                    # If delete that node as last node
        else:
            current = self.head                 # Assign head as current
            previous = None

            # Go to the forward using while loop to find last node
            while current.getNext()is not None:
                previous = current              # Get the previous node of the current
                current = current.getNext()     # Get next node relevant to the current (last node)

            previous.setNext(None)              # Previous node's set next assign to the none
        self.length -= 1

    # Delete a node at the given position of the list

    def deleteNodeByPos(self, Pos):

        if self.head is None:                   # Check the list is empty
            print("Empty link list")

        # Check the given position between the list
        if self.length > Pos > -1:              # If given position is  between the list,

            if Pos == 0:                        # Check the given position is equal to the zero (head position)
                self.deleteFirstNode()          # If given position is equal to the zero then delete the first node
            elif Pos == self.length-1:          # Check the given position is equal to length-1 (last node position)
                self.deleteLastNode()           # If given position is equal to the length-1 then delete the last node

            else:

                count = 0
                current = self.head             # Assign head as current

                # Go to the forward using while loop to find given node
                while count != Pos - 1:
                    count += 1
                    current = current.getNext()         # Get next node relevant to the current

                deletingNode = current.getNext()        # Get current's next node as deleting node
                nextNode = deletingNode.getNext()       # Get deleting node's next node as next node
                prevoiusNode = deletingNode.getPrev()   # Get deleting node's previous node as previous node
                prevoiusNode.setNext(nextNode)          # Previous node's set next point to the next node
                nextNode.setPrev(prevoiusNode)          # Next node's set previous point to previous node
                self.length -= 1

# Search the data by using given position

    def searchDatabyPos(self, Pos ):

        if self.head is None:                           # Check the list is empty
            print("Empty Link List")

        # Check the given position between the list
        if self.length > Pos > -1:                  # If given position is  between the list,

            if Pos == 0:                            # Check the given position is equal to the zero (head position)
                print(self.head.getData())          # Search node is first node then get data of the first node
            elif Pos == self.length-1:              # Check the given position is equal to length-1 (last node position)
                current = self.head                 # Assign head as current

                # Go to the forward using while loop to find last node
                while current.getNext() is not None:
                    current = current.getNext()     # Get next node relevant to the current
                lastNode = current                  # Current node assign to the last node
                print(lastNode.getData())           # Search node is last node then get data of the last node
            else:
                count = 0
                current = self.head                 # Assign head as current

                # Go to the forward using while loop to find given node
                while count != Pos - 1:
                    count += 1
                    current = current.getNext()     # Get next node relevant to the current
                posNode = current.getNext()         # Get search node as pos Node
                print(posNode.getData())            # Get search node data

# Search the next and previous data relevant to the given position

    def searchNextPrevByPos(self, Pos):

        if self.head is None:                       # Check the list is empty
            print("Empty Link List")

        # Check the given position between the list
        if self.length > Pos > -1:                  # If given position is  between the list,
            if Pos == 0:                            # Check the given position is equal to the zero (head position)
                print("It have not previous node and next node ")   # List has one element

            elif Pos == self.length-1:              # Check the given position is equal to length-1 (last node position)
                current = self.head                 # Assign head as current

                # Go to the forward using while loop to find last node
                while current.getNext() is not None:
                    current = current.getNext()     # Get next node relevant to the current
                prevNode = current.getPrev()        # Get previous node relevant to the current
                print(prevNode.getData())           # Get previous node data
                print("It has not next node")       # Last node has not next node
            else:
                count = 0
                current = self.head                 # Assign head as current

                # Go to the forward using while loop to find given node
                while count != Pos - 1:
                    count += 1
                    current = current.getNext()     # Get next node relevant to the current
                current = current.getNext()         # Get the given node
                prevNode = current.getPrev()        # Get the previous node
                nextNode = current.getNext()        # Get the last node
                print(prevNode.getData())           # Get previous node data
                print(nextNode.getData())           # Get last node data






