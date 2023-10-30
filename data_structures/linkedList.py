"""
## Linked List

Sequential list of nodes that holds data which point to other nodes also
containing data.

Usage:
- List, Queue, and Stack Implementation
- Circular Lists
- Can easily model real world objects like a train
- Used in separate chaining, which is present in some hash table
  implementations to deal with hashing collisions
- Often used for adjacency lists in graphs

Types:
- Singly Linked
  - Pros:
    - Uses Less Memory
    - Simpler implementation
  - Cons:
    - Cannot easily access previous elements
- Doubly Linked
  - Pros:
    - Can be traversed backward
  - Cons:
    - Takes 2x memory
"""
from nodes import Node
from nodes import BidirectionalNode


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        stringOutput = ""

        # traverse list and print all values
        currNode = self.head
        i = 0
        while currNode:
            stringOutput += f"{currNode.value} "
            currNode = currNode.next
            i += 1

        return stringOutput.strip()

    def append(self, value):
        """Append new node with value 'value' at end of list"""
        newNode = Node(value)

        # set old tail node to point to new node
        if self.tail:
            self.tail.next = newNode

        # set list tail pointer to point to new node
        self.tail = newNode

        # special case, first addition to list
        if not self.head:
            self.head = newNode

        return newNode

    def prepend(self, value):
        """Prepend node with new value to beginning of list"""
        newNode = Node(value)

        newNode.next = self.head

        # edge case, empty list
        if self.tail is None:
            self.tail = newNode

        self.head = newNode

        return newNode

    def insertAt(self, positionValue, newValue):
        """Insert node with newValue before first node with value
        positionValue. Returns newly created Node if successful"""

        # if no nodes in list, return False
        if not self.head:
            return None

        # edge case, inserting at beginning of list
        if self.head.value == positionValue:
            newNode = Node(newValue)
            newNode.next = self.head
            self.head = newNode
            return newNode

        # traverse list until one node before node with positionValue
        currNode = self.head
        while currNode.next and currNode.next.value != positionValue:
            currNode = currNode.next

        # if end of list reached, return None
        if not currNode.next:
            return None

        newNode = Node(newValue)

        # redirect two pointers to newNode
        newNode.next = currNode.next
        currNode.next = newNode

        return newNode

    def deleteAt(self, positionValue):
        """
        Delete first node with positionValue, returns deleted node if
        successful and None if unsuccessful.
        """
        # edge case, empty list
        if not self.head:
            return None

        # init two pointers to traverse
        trav1 = self.head
        trav2 = self.head.next

        # edge case, removing fist node
        if trav1.value == positionValue:
            self.head = trav1.next
            if self.tail == trav1:
                self.tail = None
            return trav1

        # shift both nodes along until trav2.value = positionValue
        while trav2 and trav2.value != positionValue:
            trav1 = trav1.next
            trav2 = trav2.next

        # no positionValue found, or list is one element long
        if not trav2:
            if trav1.value == positionValue:
                self.head = None
                self.tail = None
                return trav1
            return None

        # edge case, removed last node
        if not trav2.next:
            self.tail = trav1

        # redirect trav1 pointer
        removedNode = trav2
        trav1.next = trav2.next

        return removedNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        stringOutput = ""

        # traverse list and print all values
        currNode = self.head
        i = 0
        while currNode:
            stringOutput += f"{currNode.value} "
            currNode = currNode.next
            i += 1

        return stringOutput.strip()

    def isEmpty(self):
        return self.head is None

    def append(self, value):
        """Append new node with value 'value' at end of list"""
        newNode = BidirectionalNode(value)

        # change tail next pointer (if exists)
        if self.tail:
            self.tail.next = newNode

        # change prev pointer of newNode and save as new tail
        newNode.prev = self.tail
        self.tail = newNode

        # edge case, first addition to list
        if not self.head:
            self.head = newNode

        return newNode

    def prepend(self, value):
        """Prepend node with new value to beginning of list"""
        newNode = BidirectionalNode(value)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        # edge case, empty list
        if self.tail is None:
            self.tail = newNode

        self.head = newNode

        return newNode

    def insertAt(self, positionValue, newValue):
        """Insert node with newValue before first node with value
        positionValue. Returns newly created Node if successful"""

        # if no nodes in list, return False
        if not self.head:
            return None

        # edge case, inserting at beginning of list
        if self.head.value == positionValue:
            newNode = Node(newValue)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return newNode

        # traverse list until one node before node with positionValue
        currNode = self.head
        while currNode.next and currNode.next.value != positionValue:
            currNode = currNode.next

        # if end of list reached, return None
        if not currNode.next:
            return None

        newNode = Node(newValue)

        # point newNode prev and next to correct nodes
        newNode.prev = currNode
        newNode.next = currNode.next

        # point nodes on either side of insertion pos to newNode
        currNode.next.prev = newNode
        currNode.next = newNode

        return newNode

    def deleteAt(self, positionValue):
        """
        Delete first node with positionValue, returns deleted node if
        successful and None if unsuccessful.
        """
        # edge case, empty list
        if not self.head:
            return None

        # init pointer to traverse
        currNode = self.head

        # traverse until curNode has positionValue or end of list
        while currNode and currNode.value != positionValue:
            currNode = currNode.next

        # no positionValue found
        if not currNode:
            return None

        # edge case, removing last node
        if not currNode.next:
            self.tail = currNode.prev

        # edge case, removing first node
        if self.head == currNode:
            self.head = currNode.next

        # redirect pointers
        removedNode = currNode
        if currNode.prev is not None:
            currNode.prev.next = currNode.next
        if currNode.next is not None:
            currNode.next.prev = currNode.prev

        return removedNode

    def removeFirst(self):
        """Removes and returns first element in list"""
        # edge case, empty
        if self.head is None:
            return None

        removedNode = self.head
        self.head = removedNode.next
        if self.head:
            self.head.prev = None

        # edge case, list is length 1
        if removedNode.next is None:
            self.tail = self.head

        return removedNode


def main():
    # singly linked list demo
    # generate dummy data and insert
    list1 = SinglyLinkedList()
    for i in range(10):
        list1.append(i)

    print(list1)

    # successful and unsuccessful insertAt
    list1.insertAt(5, 10)
    list1.insertAt(11, 10)

    print(list1)

    # successful and unsuccessful delete
    list1.deleteAt(10)
    list1.deleteAt(11)

    print(list1)


if __name__ == "__main__":
    main()
