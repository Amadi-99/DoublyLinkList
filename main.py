import DoublyLinkList


LinkedList = DoublyLinkList.DoublyLinkedList()

# Insert the data for beginning,end and given position

LinkedList.addNodeBeginning(30)
LinkedList.addNodeBeginning(20)
LinkedList.addNodeBeginning(10)
LinkedList.addNodeEnd(40)
LinkedList.addNodeEnd(50)
LinkedList.addNodeEnd(60)
LinkedList.addNodeInPos(6, 70)
LinkedList.addNodeInPos(7, 80)

# print Doubly Link List

print("Doubly Link List \n\nInsert the data in beginning, end and given position ")
LinkedList.printList()
print("\n")

# Traversing forward and backward methods of the Doubly Link List

print("Traversing to Forward and Backward \n ")
LinkedList.printListForward()
print("\n")
LinkedList.printListReverse()
print("\n")

# Delete the data in beginning,end and given position

print(" Delete the data in beginning, end and given position \n ")

LinkedList.deleteFirstNode()
LinkedList.deleteLastNode()
LinkedList.deleteNodeByPos(1)
LinkedList.printList()
print(" \n ")


# Search the data by using given position

print(" Search the data by using given position \n ")
LinkedList.searchDatabyPos(1)
print(" \n ")

# Search the next and previous data relevant to the given position

print(" The next and previous data relevant to the given position\n ")
LinkedList.searchNextPrevByPos(1)
